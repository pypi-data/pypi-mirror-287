from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx.util.docutils import SphinxDirective
import matplotlib.pyplot as plt
import os

from stacksim.stack import Stack
from stacksim.stackSession import StackSession
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

        for line in self.content:
            session.parseCommand(line)

        style = """
        <style type="text/css">
        .ansi2html-content {
            display: inline;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-size: 0.8em;
            font-weight: bold
            line-height: 0.1;
            margin: 0;
            padding: 0;
        }
        .container { width: 80%;}
        .body_foreground { color: #AAAAAA; }
        .body_background { background-color: #000000; }
        .inv_foreground { color: #000000; }
        .inv_background { background-color: #AAAAAA; }
        .ansi32 { color: #00aa00; }
        .ansi33 { color: #aa5500; }
        .ansi34 { color: #0000aa; }
        .ansi90 { color: #7f7f7f; }
    </style>
        """
        
        html_content = session.stack.toHtml(showAddress=show_addresses, full=False)

        html_content = f'<div class="container"><pre class="ansi2html-content">{html_content}</pre></div>'
        raw_html_node = nodes.raw('', style + "\n"+html_content, format='html')
        return [raw_html_node]
    



def generate_stack_image(stack, base_address, show_addresses, env):
    fig, ax = plt.subplots()

    ax.axis('off')
    y_offset = 0.8

    for index, item in enumerate(stack):
        address = f'{int(base_address, 16) + index * 4:#010x}'
        text = f'{address}: {item}' if show_addresses else item
        ax.text(0.5, y_offset, text, horizontalalignment='center', verticalalignment='center', fontsize=12)
        y_offset -= 0.2

    image_path = os.path.join(env.app.outdir, 'stack_image.png')
    plt.savefig(image_path)
    plt.close(fig)
    
    return image_path

def setup(app):
    app.add_directive('stack', StackDirective)
