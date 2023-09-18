import os
import shutil
from setuptools import setup


OUTPUT_DIR = 'output'


if __name__ == "__main__":
    setup(
        name="esg_risk_training",
        packages=['esg_risk_training'],
        version="0.0.1",
        script_args=['--quiet', 'bdist_egg'], # to create egg-file only
    )

    egg_name = os.listdir('dist')[0]

    os.rename(
        os.path.join('dist', egg_name),
        os.path.join(OUTPUT_DIR, egg_name)
    )

    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('my_module.egg-info')
