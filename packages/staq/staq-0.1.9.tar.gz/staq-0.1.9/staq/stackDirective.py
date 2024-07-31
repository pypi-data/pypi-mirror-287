from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxDirective
import matplotlib.pyplot as plt
import os


from staq.stack import Stack
from staq.stackSession import StackSession
import yaml

class StackDirective(SphinxDirective):
    has_content = True
    option_spec = {
        'baseAddress': directives.unchanged,
        'showAddress': directives.flag,
    }


    def run(self):
        base_address = self.options.get('baseAddress', '0x0')
        show_addresses = 'showAddress' in self.options

        session = StackSession()


        contents= '\n'.join(self.content)

        contentHash = str(abs(hash(contents)))
        output_dir = self.state.document.settings.env.app.outdir

        for line in self.content:
            session.parseCommand(line)

        # Get the Sphinx builder
        builder = self.state.document.settings.env.app.builder.name

        if builder == 'html':
            html_content = session.stack.toHtml(showAddress=show_addresses, full=False)
            raw_html_node = nodes.raw('',html_content, format='html')
            return [raw_html_node]
        elif builder == 'latex' or builder == 'latexpdf':

            #print to build output 
            print(f"[stack] content hash: {contentHash}")
            print(f"[stack] image path: {image_path}")
            image_name = f"stack_{contentHash[:8]}.png"
            image_path = os.path.join(output_dir, image_name)
            session.stack.generatePng(image_path)


            # # Ensure the image is available for LaTeX builder
            # self.state.document.settings.env.app.config.add_latex_package('graphicx')

            image_node = nodes.image(uri=image_path)
            return [image_node]
        else:
            warning_node = self.state.document.reporter.warning(
                f'Unsupported builder: {builder}', line=self.lineno
            )
            return [warning_node]

    



def generate_stack_image(stack, base_address, show_addresses, env, contentHash):
    

    image_path = os.path.join(env.app.outdir, f"stack_{contentHash}.png")
    stack.generatePng(image_path)

    
    return image_path

def setup(app):
    app.add_directive('stack', StackDirective)
