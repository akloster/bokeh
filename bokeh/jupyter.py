from IPython.html import widgets
from IPython.utils.traitlets import Unicode
from bokeh.protocol import serialize_json


class JupyterAnimationWidget(widgets.DOMWidget):
    _view_module = Unicode('bokeh_jupyter', sync=True)
    _view_name = Unicode('JupyterAnimationWidget', sync=True)

    def __init__(self, *args, **kwargs):
        widgets.DOMWidget.__init__(self,*args, **kwargs)
        self.on_msg(self._handle_custom_msg)

    def replace_bokeh_data_source(self, ds):
        self.send({"custom_type": "replace_bokeh_data_source",
                "ds_id": ds.ref['id'], # Model Id
                "ds_model":ds.ref['type'], # Collection Type
                "ds_json": serialize_json(ds.vm_serialize())
        })
