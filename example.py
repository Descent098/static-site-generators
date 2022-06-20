from ezprez.core import *
from ezprez.components import *

# What is an SSG
Slide("What is a static site generator?", "A static site generator is a system that allows you to create a website using a template and a set of data. You can think about this as translating/transpiling data from a language or languages to a website. Universally SSG's have 3 parts:",["The source/state/content files (or sometimes a single file)", "The template file(s)",  "The output file(s)"], background="facebook")
Slide("Why use a SSG?", ["Easier to maintain than a static site", "More configurable than a static site", "cheaper and less complex than a dynamic site (i.e. wordpress)"], background="facebook")

# Principles of an SSG
Slide("Principles of an SSG", "There are some common principles that static site generators use that are important to be aware of", background="gray")
Slide("State driven templating", "This is the concept that unlike a typical 'static' site there is some sort of state used in conjunction with predefined templates to drive generating the output files", background="gray")
Slide("State driven templating", Image("ssg-explainer", "ssg-explainer.png"), background="gray")

## Ezcv example
Slide("Ezcv","This example is using ezcv, here are some links if you're interested", Link("Ezcv Source","https://github.com/Descent098/ezcv", color="#0000ff") ,Link("Ezcv Docs", "https://ezcv.readthedocs.io/en/latest/", color="#ff0000"), background="gray")
Slide("Example (Ezcv)", Image("data-transformation", "data-transformation.png"), background="gray")

## Explaining the different file types
Slide("Source files", "Source files are typically human-readable files (though don't have to be) and are used to drive the state of the template files. They are often Markdown or rich source text files, along with some sort of configuration file in JSON, YAML or TOML", Image("ezcv-config","ezcv-config.png"), Image("ezcv-md","ezcv-md.png"), background="gray")
Slide("Template files", "These files are typically HTML-like files that use templating languages to pull data from the source files and generate output files",Image("ezcv-template","ezcv-template.png"), background="gray")
Slide("Output files", "These files are the result at the end that can be hosted somewhere. These will typically be HTML/CSS/JS files along with any additional static files like images.",Image("ezcv-output","ezcv-output.png"), background="gray")

## Markup Transformation
Slide("Markup transformation", "Lost of SSG's are built on the principle that markup systems (like HTML) are used to express common structures and content. With this the specifics of one system are often analogous to another which means you can convert them 1 to 1 from one form to another (i.e. markdown to HTML)", background="black")
Slide("Markup transformation", Image("compare-markup", "compare-markup.png"), background="black")
Slide("This does not work in all cases", Image("exception", "exception.png"), background="black")

# Using this presentation as an example of an SSG
Slide("Another example of a SSG would be this presentation", "This presentation is built using the ezprez framework. It is a static site generator that uses python to generate HTML files", Link("Ezprez Source", "https://github.com/Descent098/ezprez", color="#54ff0a") ,Link("Ezprez Docs", "https://ezprez.readthedocs.io/en/latest/"),Link("Presentation Source", "https://github.com/Descent098/static-site-generators", color="#ff0000"), background="black")
## Explaining the different file types
Slide("Source files", "The source file(s) are written in python using .py files", background="black")
ezprez_example_snippet = """from ezprez.core import Slide, Presentation
from ezprez.components import *

# Creating a slide
Slide('Source Files', 'The source file(s) are written in python using .py files', background='black')

# Presentation settings
title = 'Static site generators'
description = 'An overview of markup transformation & Static Site Generator (SSG) demo'
url = 'https://kieranwood.ca/static-site-generators'

prez = Presentation(title, description, url)
prez.export('.', force=True, folder_name='Presentation') # Export to ./Presentation
"""
Slide("Example source for the last slide", Code("python", ezprez_example_snippet), background="black")
Slide("Template files", "In Ezprez the template files are obfuscated from you and are part of the library itself. They still exist, you just can't interact with them.", background="black")
Slide("Output files", "In this case Ezprez will export out an index.html file which is the presentation and several folders", Image("ezprez-dir", "ezprez-dir.png"), background="black")

# Using hugo
Slide("Hugo", "We use hugo for schulich ignite",Link("Hugo Source", "https://github.com/gohugoio/hugo", color="#54ff0a") ,Link("Hugo Docs", "https://gohugo.io/documentation/"),Link("Ignite Site Source", "https://github.com/Schulich-Ignite/website", color="#ff0000"), background="black-blue")
Slide("Hugo overview", "Hugo uses markdown files for content and TOML files for configuration", background="black-blue")
#TODO: Add a link to the hugo docs & other hugo stuff

## Explaining the different file types in hugo

### Source files extra info (markdown basics, frontmatter, datetime info, available plugins etc.)
Slide("Source files", "Hugo uses markdown files for content and TOML files for configuration", background="black-blue")
Slide("Example source files", "", background="black-blue")

### Template files extra info (template filters, partials, context passing etc.)
Slide("Template files", "Hugo does not have a seperate file type for template or output files, both are .html files", background="black-blue")
Slide("Example Template files", "", background="black-blue")

### Output files extra info (Can be exported to a folder, can be served)
Slide("Output files", "Hugo will output HTML/CSS/jS files", background="black-blue")
Slide("Example Output files", "", background="black-blue")


# Setup the presentation
presentation_title = "Static site generators"
presentation_description = "An overview of markup transformation & Static Site Generator (SSG) demo" 
presentation_url = "https://kieranwood.ca/static-site-generators" # TODO: Fill in with the url of your presentation
prez = Presentation(presentation_title, presentation_description, presentation_url, image=Image("intro", "intro.png"))

# Export the files to the current directory at /Presentation, do not change this if you want to use the auto-deployment
prez.export(".", force=True, folder_name="Presentation")
