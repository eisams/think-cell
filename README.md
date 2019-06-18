# thinkcell <img src="assets/logo.png" width="30">
[![Build Status](https://travis-ci.org/duarteocarmo/think-cell.svg?branch=master)](https://travis-ci.org/duarteocarmo/think-cell) [![GitHub license](https://img.shields.io/github/license/duarteocarmo/think-cell.svg)](https://github.com/duarteocarmo/think-cell/blob/master/LICENSE) [![Coverage Status](https://coveralls.io/repos/github/duarteocarmo/think-cell/badge.svg?branch=master)](https://coveralls.io/github/duarteocarmo/think-cell?branch=master)

thinkcell is a simple library that helps you automatically generate presentations in an quick and simple way. 

In order to use it you will need a valid and working [think-cell license and installation](https://www.think-cell.com/en/). 

### Installation

thinkcell is available on PyPi. 

```console
 $ pip install thinkcell
 ```

### Tutorial and Usage

Let us say you have generated a template `template.pptx` according to [think-cell's automation guidelines](https://www.think-cell.com/en/support/manual/jsondataautomation.shtml) called `simple-template.pptx` with the following chart called `Chart1`: 

<center>
<img src="assets/example.png" width="500">
</center>

The thinkcell library helps you generate a `.pptc` file so that you can generate presentations based on that template using python:

```python
from thinkcell import Thinkcell

template_name = "simple-template.pptx"
categories = ["Ads", "Revenue", "Losses"]
chart_name = "Chart1"
filename = "simple-example.ppttc"

data = [["Amazon", 1, 11, 14], ["Slack", 8, 2, 15], ["Ford", 1, 2, 12]]

tc = Thinkcell() # create thinkcell object
tc.add_template(template_name) # add your template
tc.add_chart(
    template_name=template_name,
    chart_name=chart_name,
    categories=categories,
    data=data,
) # add you categories and data

tc.save_ppttc(filename=filename)
 ```

Once done, go ahead and double click the generated `simple-example.pptc` file, and your chart will open. Save it and you are done!

Visit the [examples folder](examples) for more examples and source files. 

If you wish to learn more about this process, visit the think-cell [automation documentation](https://www.think-cell.com/en/support/manual/jsondataautomation.shtml). 

### Contributing

Start by forking this repo.


Install the development dependencies (you probably want to do this in a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/)):

```console
 $ pip install -r requirements-dev.txt
 ```

Make sure the tests run:

```console
 $ pytest
 ```

Then you can create a branch and submit a pull request. 


### Progress and Todos

To do:
- [x] Make complex examples
- [x] Finish readme
- [x] Continuous integration
- [ ] Pypi