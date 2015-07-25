if IPython?
  window.define("bokeh_jupyter", ["jquery", "widgets/js/widget"], ($, widget)->
    JupyterAnimationWidget =  widget.DOMWidgetView.extend(
       render: ()->
         html = $("<p>Bokeh Animation Manager</p>")
         @setElement(html);
         @model.on('msg:custom', $.proxy(@handle_custom_message, this))
       handle_custom_message: (data)->
         switch
           when (data.custom_type == "replace_bokeh_data_source")
             ds = Bokeh.Collections(data.ds_model).get(data.ds_id)
             ds.set($.parseJSON(data.ds_json))
             ds.trigger("change")
    )
    return {
      JupyterAnimationWidget: JupyterAnimationWidget
    }
  )
