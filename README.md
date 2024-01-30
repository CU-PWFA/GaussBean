# Welcome to GaussBean!

## A *GAUSS*ian *BE*am *AN*alysis package, originally made for analysis of passive plasma lens data in the CU WARG group.

### Before Installing

Before you try to install GaussBean, make sure that you have Anaconda (or some fork of Anaconda, such as Miniconda or Mamba) installed. Instructions on how to install each of those are given at the links below:

Anaconda: https://docs.anaconda.com/free/anaconda/install/index.html
Miniconda: https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html
Mamba: https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html

If those links don't work, you should be able to just Google "____ installation" and find out how to install any of those distributions.

### Dependencies

There are dependencies needed for GaussBean, but when installing the package itself, the installer should install all the necessary dependencies if they are not already installed on your system.

### Installation

GaussBean was originally built using Anaconda, so once you have the Anaconda (or forked) distribution installed (as mentioned above), go to your <ins>terminal</ins> and use Git to clone GaussBean from this repository:

'''
git clone https://github.com/CU-PWFA/GaussBean.git
'''

Now, from your terminal, navigate to the top level of the directory where GaussBean was cloned (if you run the command "ls -a," you should see a file named "gaussbean.yml"; if you don't see this file, you are not at the top level of the directory) and run the following command:

'''
conda env create -f gaussbean.yml
'''

This command *should* create a conda (or mamba) environment named "gaussbean". If you are using JupyterLab or a single Jupyter Notebook, you can use the following command in your terminal to install <ins>ipykernel</ins> (or, skip this step if it's already installed on your system; also, note that this is *NOT necessary* in order to use this package, it just makes things easier):

'''
python3 -m pip install ipykernel
'''

Now, you can run the following command (also in your terminal) to add the GaussBean package as a kernel 

### Using GaussBean

If you want and example of how to use GaussBean, you can take a look into the "examples" folder in the GitHub repository, where you should find an example Jupyter Notebook that goes through *most* of the functionality of the package.

If you have questions, there is lots of documentation both in the .py files themselves (inputs, function purposes, comments, etc.) as well as in the example notebook previously mentioned. If you want to raise a concern about code or an issue, you can open an issue on GitHub, or just contact any of the contributors to the package.

* Uninstalling

To uninstall GaussBean, 
