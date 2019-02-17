# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.0.0-rc5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] {"toc": true, "slideshow": {"slide_type": "slide"}}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Part-1----Infrastructure" data-toc-modified-id="Part-1----Infrastructure-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Part 1 -- Infrastructure</a></span></li><li><span><a href="#Part-2----Examples" data-toc-modified-id="Part-2----Examples-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Part 2 -- Examples</a></span></li><li><span><a href="#Some-history" data-toc-modified-id="Some-history-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Some history</a></span></li><li><span><a href="#Infrastructure" data-toc-modified-id="Infrastructure-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Infrastructure</a></span><ul class="toc-item"><li><span><a href="#Linux-kernel" data-toc-modified-id="Linux-kernel-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Linux kernel</a></span></li><li><span><a href="#Git-and-Github" data-toc-modified-id="Git-and-Github-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Git and Github</a></span></li><li><span><a href="#Conda-forge" data-toc-modified-id="Conda-forge-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Conda-forge</a></span></li><li><span><a href="#Jupyter-and-jupytext" data-toc-modified-id="Jupyter-and-jupytext-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Jupyter and jupytext</a></span></li><li><span><a href="#Cocalc,-nbgrader-and-nbsphinx" data-toc-modified-id="Cocalc,-nbgrader-and-nbsphinx-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Cocalc, nbgrader and nbsphinx</a></span></li></ul></li><li><span><a href="#Examples" data-toc-modified-id="Examples-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Examples</a></span><ul class="toc-item"><li><span><a href="#Inspiration" data-toc-modified-id="Inspiration-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Inspiration</a></span></li><li><span><a href="#Large-class,-2nd-year" data-toc-modified-id="Large-class,-2nd-year-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Large class, 2nd year</a></span></li><li><span><a href="#Smaller-class,-3rd-and-4th-year" data-toc-modified-id="Smaller-class,-3rd-and-4th-year-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Smaller class, 3rd and 4th year</a></span></li><li><span><a href="#Grad/post-doc-workshop" data-toc-modified-id="Grad/post-doc-workshop-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Grad/post-doc workshop</a></span></li></ul></li><li><span><a href="#What's-next?" data-toc-modified-id="What's-next?-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>What's next?</a></span></li></ul></div>

# %% {"slideshow": {"slide_type": "skip"}}
from IPython.display import Image

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Computational instruction with Jupyter notebooks
#
# Philip Austin, Department of Earth, Ocean and Atmospheric Sciences, UBC
#
# Notebook available at https://github.com/phaustin/mcgill_2019_talk

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Part 1 -- Infrastructure
#
# * Linux/git
# * Conda-forge
# * Jupyter/Jupytext
# * Cocalc
# * nbgrader
# * nbsphinx
# * pangeo

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ## Part 2 -- Examples
#
# * 2nd year course, 48 students
#   - Jupyter/chrome/cocalc
# * 3rd/4th year course, 26 students 
#   - Jupyter/laptops/conda-forge
# * Grad/postdoc workshop, 20 students, 
#   - pangeo with dask/xarray,zarr on an HPC cluster
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Some history
#
# **July, 1997: BAMS article: John Stockie, Susan Allen, Phil Austin**
#
# *An Interactive Course in Numerical Methods for the Earth Sciences*

# %% {"slideshow": {"slide_type": "subslide"}}
Image(filename='figures/bams_ref.png')

# %% [markdown] {"trusted": false, "slideshow": {"slide_type": "slide"}}
# ## Infrastructure
#
# ### Linux kernel 
#
# * developed by 19,000 unique committers
#
# * 65,000 files
#
# * 25 million lines of code

# %% [markdown] {"trusted": false, "slideshow": {"slide_type": "subslide"}}
# ### Git and Github
#
# * 2005: [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) begins [Git development](https://en.wikipedia.org/wiki/Git) 
#
# * 2008: [Github founded](https://en.wikipedia.org/wiki/GitHub), in 2018 it hosted 28 million users and 57 million repositories
# * Distributed version control makes possible the:
#     - [pull request workflow](https://yangsu.github.io/pull-request-tutorial/)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Conda-forge
#
# * Software packaging using [conda](https://conda.io/projects/conda/en/latest/index.html)
#
# * Supported by [numfocus](https://numfocus.org/project/conda-forge) -- provides scientifc software 
#   for linux, macos and windows 10 ~ 3500 separate packages
#   
#   - [netcdf-fortran feedstock](https://github.com/conda-forge/netcdf-fortran-feedstock)
#   
#   - [gdal feedstock](https://github.com/conda-forge/gdal-feedstock)
#

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Jupyter and jupytext
#
# * [Jupyter](https://blog.jupyter.org/jupyter-receives-the-acm-software-system-award-d433b0dfe3a2)
#
#   - Origins -- began in 2001 as ipython: repl (read, evaluate, print, loop)
#   
#   - [Hosts 100 language kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
#   
# * [jupytext](https://github.com/mwouts/jupytext)
#   - round trip conversion between jupyter notebooks written in javascript and 
#     
#     - python, R, markdown, Julia, bash scripts
#     
#     - Allows collaborative notebook development uisng pull-requests
#     
#     - Example: [this talk](https://github.com/phaustin/mcgill_2019_talk/blob/master/talk_dir/python/mcgill_talk.py)

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Cocalc, nbgrader and nbsphinx
#
# * [cocalc.com](https://cocalc.com): juypter notebook hosting for classes
#
# * [nbgrader](https://github.com/jupyter/nbgrader): autograded jupyter notebooks
#
# * [nbsphinx](https://github.com/spatialaudio/nbsphinx): build a webstie from notebooks

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "trusted": false}
# ## Examples

# %% [markdown] {"slideshow": {"slide_type": "fragment"}, "trusted": false}
# ### Inspiration
#
#   - [Cliburn Chan's Stat 663](http://people.duke.edu/~ccc14/sta-663-2018/index.html)
#   - [Berkeley's data 8](https://data.berkeley.edu/education/courses/data-8)

# %% [markdown] {"slideshow": {"slide_type": "fragment"}, "trusted": false}
#   
# ### Large class, 2nd year
#
# * [Computational Methods in Geological Engineering](https://phaustin.github.io/eosc213/)
#   - co-taught with Roger Beckie and Nicolas Seigneur
#   - 48 2nd year geological engineering students
#   - Prereqs: vector calculus, linear algebra, C
#   - students use: cocalc.com notebooks

# %% [markdown] {"slideshow": {"slide_type": "subslide"}, "trusted": false}
# ### Smaller class, 3rd and 4th year
#   
# * 3rd/4th year: [Radiation and remote sensing](https://phaustin.github.io/a301_code/)  
#   - taught to 26 students in EOSC and other departments
#   - open to any student with 1st year calculus, physics, programming
#   - includes both jupyter notebooks and course libraries
#   - students ues: conda environments on laptops or lab desktops
#   

# %% [markdown] {"slideshow": {"slide_type": "subslide"}}
# ### Grad/post-doc workshop
#
# * [Parallel python tutorial](https://phaustin.github.io/parallel_python_course/)
# * Introduce the [pangeo software stack](https://docs.google.com/presentation/d/1evNXCddIllXUt4a5jKfmlO2197sp8T6I9L650cYZcsk/edit#slide=id.g4f72134f6b_0_84),
#   particularly [dask](http://docs.dask.org/en/latest/), [xarray](https://xarray.pydata.org/en/stable/) and [zarr](https://zarr.readthedocs.io/en/stable/). (see this [pangeo notebook server](https://binder.pangeo.io/))
# * 20 UBC HPC focussed grad students/postdocs
# * Half day, using notebooks and Compute Canada cluster

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## What's next?
#
#
# * I am writing an instructor's guide to teaching with Jupyter notebooks
#
# * I'd like to explore collaborative notebook development for UCAR member institutions via the UCAR members mailing list
#
# * Questions/interest/want to help?  Email me at paustin@eoas.ubc.ca
#
# > "The future is already here — it's just not very evenly distributed." -- William Gibson

# %%

# %%
