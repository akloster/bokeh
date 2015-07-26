if IPython?
  window.define "bokeh_jupyter", ["jquery", "widgets/js/widget"], ($, widget)->
    JupyterAnimationWidget =  widget.DOMWidgetView.extend
       render: ()->
         html = $("<p>Bokeh Animation Manager</p>")
         @setElement(html)
         @selectables = {}
         @model.on('msg:custom', $.proxy(@handle_custom_message, @))
       handle_custom_message: ((data)->
         ct = data.custom_type
         if ct == "replace_bokeh_data_source"
           ds = Bokeh.Collections(data.ds_model).get(data.ds_id)
           ds.set($.parseJSON(data.ds_json))
           ds.trigger("change")
         if ct == "make_selectable"
           ds = Bokeh.Collections(data.ds_model).get(data.ds_id)
           unless @selectables[data.ds_id]
             @selectables[data.ds_id] = ds
             ds.on("select",=>
                         @send({
                            'msg_type':'select',
                            'ds_id': data.ds_id,
                            'selected': ds.get('selected')
                         })
              , {widget:this, ds: ds})
         )
    return {
      JupyterAnimationWidget: JupyterAnimationWidget
    }
