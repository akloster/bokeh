from IPython.html import widgets
from IPython.utils.traitlets import Unicode
from bokeh.protocol import serialize_json


class JupyterAnimationWidget(widgets.DOMWidget):
    _view_module = Unicode('bokeh_jupyter', sync=True)
    _view_name = Unicode('JupyterAnimationWidget', sync=True)

    def __init__(self, *args, **kwargs):
        widgets.DOMWidget.__init__(self,*args, **kwargs)
        self.selectables = dict()
        self.on_msg(self._handle_custom_msg)

    def replace_bokeh_data_source(self, ds):
        self.send({"custom_type": "replace_bokeh_data_source",
                "ds_id": ds.ref['id'], # Model Id
                "ds_model":ds.ref['type'], # Collection Type
                "ds_json": serialize_json(ds.vm_serialize())
        })

    def _handle_custom_msg(self, content):
        msg_type = content['msg_type']
        if msg_type == 'select':
            try:
                ds = self.selectables[content['ds_id']]
                ds.selected = content['selected']
            except KeyError:
                print("Datasource not found/connected")

    def make_selectable(self, ds):
        self.selectables[ds.ref['id']] = ds
        self.send({"custom_type": "make_selectable",
                "ds_id": ds.ref['id'], # Model Id
                "ds_model":ds.ref['type'], # Collection Type
        });
