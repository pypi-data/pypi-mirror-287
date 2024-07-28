import os
import sys
import json
import click
import pandas
import tables
import random
import warnings
import numpy as np

#from hydra_pywr import *
from pywr.model import Model
from .moea import SaveNondominatedSolutionsArchive
from pywr.recorders.progress import ProgressRecorder
from .custom_parameters_and_recorders import *

import logging
logger = logging.getLogger(__name__)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('filename', type=click.Path(file_okay=True, dir_okay=False, exists=True))
def run(filename):
    
    path = os.path.join("outputs")
    os.makedirs(path, exist_ok=True)

    """ Run the Pywr model. """
    logger.info('Loading model from file: "{}"'.format(filename))
    model = Model.load(filename)

    warnings.filterwarnings('ignore', category=tables.NaturalNameWarning)

    ProgressRecorder(model)

    logger.info('Starting model run.')
    ret = model.run()
    logger.info(ret)

    try:
        df = model.to_dataframe()

        fn = '{}/{}.csv'.format("outputs","water_results_time_step")
        i=1
        while os.path.isfile(os.path.join(os.getcwd(), fn)):
            fn = '{}/{}_{}.csv'.format("outputs","water_results_time_step", str(i))
            i+=1
        df.to_csv(fn)
    except:
        pass


@cli.command()
@click.argument('filename', type=click.Path(file_okay=True, dir_okay=False, exists=True))
@click.option('-s', '--seed', type=int, default=None)
@click.option('-p', '--num-cpus', type=int, default=None)
@click.option('-n', '--max-nfe', type=int, default=1000)
@click.option('--pop-size', type=int, default=50)
@click.option('-a', '--algorithm', type=click.Choice(['NSGAII', 'NSGAIII', 'EpsMOEA', 'EpsNSGAII']), default='NSGAII')
@click.option('-e', '--epsilons', multiple=True, type=float, default=(0.05, ))
@click.option('--divisions-outer', type=int, default=12)
@click.option('--divisions-inner', type=int, default=0)
def search(filename, seed, num_cpus, max_nfe, pop_size, algorithm, epsilons, divisions_outer, divisions_inner):
    import platypus

    logger.info('Loading model from file: "{}"'.format(filename))
    directory, model_name = os.path.split(filename)
    output_directory = os.path.join(directory, 'outputs')

    if algorithm == 'NSGAII':
        algorithm_klass = platypus.NSGAII
        algorithm_kwargs = {'population_size': pop_size}
    elif algorithm == 'NSGAIII':
        algorithm_klass = platypus.NSGAIII
        algorithm_kwargs = {'divisions_outer': divisions_outer, 'divisions_inner': divisions_inner}
    elif algorithm == 'EpsMOEA':
        algorithm_klass = platypus.EpsMOEA
        algorithm_kwargs = {'population_size': pop_size, 'epsilons': epsilons}
    elif algorithm == 'EpsNSGAII':
        algorithm_klass = platypus.EpsNSGAII
        algorithm_kwargs = {'population_size': pop_size, 'epsilons': epsilons}
    else:
        raise RuntimeError('Algorithm "{}" not supported.'.format(algorithm))

    if seed is None:
        seed = random.randrange(sys.maxsize)

    search_data = {'algorithm': algorithm, 'seed': seed, 'user_metadata':algorithm_kwargs}
    wrapper = SaveNondominatedSolutionsArchive(filename, search_data=search_data, output_directory=output_directory,
                                                   model_name=model_name)

    if seed is not None:
        random.seed(seed)

    logger.info('Starting model search.')

    if num_cpus is None:
        evaluator_klass = platypus.MapEvaluator
        evaluator_args = ()
    else:
        evaluator_klass = platypus.ProcessPoolEvaluator
        evaluator_args = (num_cpus,)

    with evaluator_klass(*evaluator_args) as evaluator:
        algorithm = algorithm_klass(wrapper.problem, evaluator=evaluator, **algorithm_kwargs, seed=seed)

        algorithm.run(max_nfe, callback=wrapper.save_nondominant)

def start_cli():
    """ Start the command line interface. """
    from . import logger
    import sys
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(stream=sys.stdout)
    logger.addHandler(ch)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    # Also log pywr messages
    pywr_logger = logging.getLogger('pywr')
    pywr_logger.setLevel(logging.INFO)
    pywr_logger.addHandler(ch)
    cli(obj={})

start_cli()
