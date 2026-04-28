# README
We will employ the commonly used workflow of using Python and Jupyter Notebooks for data science during this course. [Learning Unit 0](learning_unit_0.ipynb) is an introduction to this workflow.

This file contains instructions on how to install Python and Jupyter Notebooks, as well as how to get everything running.

## Prerequisites
Please make sure that you have [Python](https://www.python.org/downloads/) and [Jupyter](https://jupyter.org/install) installed on your machine. The exercise files have been tested with python version `3.9.7`. If you have trouble running the exercise files, try using this version.

### Anaconda
If these tools are new to you, the simplest way to get everything running is by using [Anaconda](https://www.anaconda.com/). This will install Python, Jupyter, and the most commonly used data science packages on your machine. You can find the install instructions for your OS [here](https://docs.anaconda.com/anaconda/install/).

## Jupyter Notebooks
The Jupyter Notebook app can be launched by typing 
```
jupyter notebook
```
inside your terminal. A new browser tab should open. You can then navigate to the `.ipynb` file on your machine and open it.

You can also start the notebook server using the Anaconda Navigator if you chose to use Anaconda.

Detailed instructions for launching a Jupyter Notebook (including how to change the startup folder) can be found [here](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html).

There are also other ways to run a Jupyter Notebook. Many editors or IDEs have support for running notebooks directly within them e.g., [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/).


## Installing Packages
For the assignments you may be required to install specific Python packages for their functionality. You can install these new packages by using [pip](https://pypi.org/project/pip/) or [conda](https://docs.conda.io/en/latest/). If you installed Anaconda, you can also do this using the Anaconda Navigator.

The corresponding terminal commands are:

```
pip install PACKAGENAME
```

or

```
conda install PACKAGENAME
```

For the Anaconda Navigator you can install additional packages inside the `Environments` tab. Make sure that you select `not installed`or `all` when you are searching for a package. Detailed instructions can be found [here](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/).