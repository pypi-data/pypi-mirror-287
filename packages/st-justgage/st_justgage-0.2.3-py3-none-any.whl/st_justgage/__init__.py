import streamlit.components.v1 as components
import os

import logging


_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_justgage",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_justgage", path=build_dir)

                                     
def st_justgage(value: int, min_value: int, max_value: int, second_value: int = None, third_value: int = None, fourth_value: int = None, fifth_value: int = None, 
    sixth_value: int = None, title: str = None, title_fontsize: int = 20, title_color: str = None, key: str = None, customCSS: str = "", id: str = "", width: int = None, 
    height: int = None, pointer: bool = True, counter: bool = True, gaugeWidthScale: float = 0.4, valueFontColor: str = 'Black', valueFontFamily: str = "Arial",
    symbol: str = "", minTxt: bool = False, maxTxt: bool = False, reverse: bool = False, textRenderer: str = None, gaugeColor: str = '#ECEAE9', label: str = "", 
    labelFontColor: str = "#b3b3b3", shadowOpacity: float = 0.2, shadowSize: int = 5, shadowVerticalOffset: int = 3, levelColors: list = ["#44546a"], startAnimationTime: int = 700,
    startAnimationType: str = ">", refreshAnimationTime: int = 700, refreshAnimationType: str = "<>", donutStartAngle: int = 90, valueMinFontSize: int = 50,
    labelMinFontSize: int = 10, minLabelMinFontSize: int = 15, maxLabelMinFontSize: int = 15, hideValue: bool = False, hideMinMax: bool = False, showInnerShadow: bool = True,
    humanFriendly: bool = False, noGradient: bool = False, donut: bool = False, differential: bool = False, relativeGaugeSize: bool = False, decimals: int = 0,
    customSectors: dict = {}, formatNumber: bool = False, pointerOptions: dict = {}, second_pointerOptions: dict = {}, third_pointerOptions: dict = {}, 
    fourth_pointerOptions: dict = {}, fifth_pointerOptions: dict = {}, sixth_pointerOptions: dict = {}, displayRemaining: bool = False,imageDataEncoded: bool = False, 
    tooltipPosition: str = 'top right', enableTooltip: str = "False", tooltipText: str = "") -> any:
    """
    Creates a JustGage display, a customizable gauge instrument, using Streamlit components. This component allows for the visualization of data within a specified range, and it can be customized extensively through various parameters including size, colors, and animations.

    Parameters
    ----------
    value : int The current value to be displayed on the gauge.
    min_value : int The minimum value of the gauge.
    max_value : int The maximum value of the gauge.
    second_value : int, optional The second value for the gauge, used if a second pointer is enabled.
    third_value : int, optional The third value for the gauge, used if a third pointer is enabled.
    fourth_value : int, optional The fourth value for the gauge, used if a fourth pointer is enabled.
    fifth_value : int, optional The fifth value for the gauge, used if a fifth pointer is enabled.
    sixth_value : int, optional The sixth value for the gauge, used if a sixth pointer is enabled.
    title : str, optional The title of the gauge.
    title_fontsize : int, optional The font size of the title.
    title_color : str, optional The font color of the title.
    key : str, optional A unique key for the element.
    customCSS : str, optional Custom CSS rules for further customization.
    id : str, optional The HTML container element ID.
    width : int, optional The width of the gauge.
    height : int, optional The height of the gauge.
    pointer : bool, optional Whether to use a pointer instead of text for the value.
    counter : bool, optional Whether to use a counter animation for the values.
    gaugeWidthScale : float, optional Scale factor for the thickness of the gauge.
    valueFontColor : str, optional The font color of the value.
    valueFontFamily : str, optional The font family of the value.
    symbol : str, optional A symbol or text to be added to the value (e.g., '%').
    minTxt : bool, optional Min value text, overrides 'min_value' if provided.
    maxTxt : bool, optional Max value text, overrides 'max_value' if provided.
    reverse : bool, optional Reverse min and max values on the gauge.
    textRenderer : str, optional A function as a string to customize the text for the gauge value.
    gaugeColor : str, optional The background color of the gauge.
    label : str, optional An additional label displayed below the value.
    labelFontColor : str, optional The font color of the label.
    shadowOpacity : float, optional The opacity of the shadow in the gauge. Range: 0 ~ 1
    shadowSize : int, optional The size of the shadow in the gauge.
    shadowVerticalOffset : int, optional The vertical offset of the shadow in the gauge.
    levelColors : list, optional The colors for the different ranges of the gauge.
    startAnimationTime : int, optional The duration of the start animation in milliseconds.
    startAnimationType : str, optional The type of animation at initialization (e.g., linear, >, <, bounce).
    refreshAnimationTime : int, optional The duration of the refresh animation in milliseconds.
    refreshAnimationType : str, optional The type of animation at refresh.
    donutStartAngle : int, optional The start angle of the gauge when 'donut' is enabled.
    valueMinFontSize : int, optional The minimum font size of the value.
    labelMinFontSize : int, optional The minimum font size of the label.
    minLabelMinFontSize : int, optional The minimum font size of the minimum value label.
    maxLabelMinFontSize : int, optional The minimum font size of the maximum value label.
    hideValue : bool, optional Whether to hide the value display.
    hideMinMax : bool, optional Whether to hide the min and max value labels.
    showInnerShadow : bool, optional Whether to display an inner shadow for visual depth.
    humanFriendly : bool, optional Whether to format numbers in a human-friendly way (e.g., '1K' instead of '1000').
    noGradient : bool, optional Whether to disable the color gradient effect.
    donut : bool, optional Whether to display the gauge as a donut shape.
    differential : bool, optional Whether to display only the difference from the previous value instead of the total.
    relativeGaugeSize : bool, optional Whether the size of the gauge should be relative to the surrounding element.
    decimals : int, optional The number of decimal places for the value.
    customSectors : dict, optional A dictionary defining custom sectors and their color ranges.
    formatNumber : bool, optional Whether to format numbers with commas as thousands separators.
    pointerOptions : dict, optional Options for customizing the pointer's appearance.
    second_pointerOptions : dict, optional Options for customizing the second pointer's appearance, if enabled.
    third_pointerOptions : dict, optional Options for customizing the third pointer's appearance, if enabled.
    fourth_pointerOptions : dict, optional Options for customizing the fourth pointer's appearance, if enabled.
    fifth_pointerOptions : dict, optional Options for customizing the fifth pointer's appearance, if enabled.
    sixth_pointerOptions : dict, optional Options for customizing the sixth pointer's appearance, if enabled.
    displayRemaining : bool, optional Whether to display the remaining value (max - value) instead of the actual value.
    imageDataEncoded : bool, optional Whether the image data is encoded.
    tooltipPosition : str, optional The position of the tooltip (e.g., 'top right').
    enableTooltip : str, optional Whether to enable a tooltip that displays additional information.
    tooltipText : str, optional The text to display inside the tooltip.

    Returns
    -------
    component_value
        The value of the component, typically used for internal purposes. This can be used to trigger actions in a Streamlit application when the gauge value changes.
    """
    #Beispiel textRenderer 
    #text_renderer_func = """
    #function(value) {
    #return value + "%";
    #}
    #"""
    if pointerOptions == {}:
        pointerOptions = {
            'toplength': -15,
            'bottomlength': 10,
            'bottomwidth': 12,
            'color': 'black',
            'stroke': '#ffffff',
            'stroke_width': 3,
            'stroke_linecap': 'round'
        }
    
    if second_pointerOptions == {}:
        second_pointerOptions = {
            'toplength': 8,
            'bottomlength': -20,
            'bottomwidth': 6,
            'color': '#8e8e93'
        }
    
    if third_pointerOptions == {}:
        third_pointerOptions = {
            'toplength': 8,
            'bottomlength': -20,
            'bottomwidth': 6,
            'color': '#8e8e93'
        }

    if fourth_pointerOptions == {}:
        fourth_pointerOptions = {
            'toplength': 8,
            'bottomlength': -20,
            'bottomwidth': 6,
            'color': '#8e8e93'
        }

    if fifth_pointerOptions == {}:
        fifth_pointerOptions = {
            'toplength': 8,
            'bottomlength': -20,
            'bottomwidth': 6,
            'color': '#8e8e93'
        }
    
    if sixth_pointerOptions == {}:
        sixth_pointerOptions = {
            'toplength': 8,
            'bottomlength': -20,
            'bottomwidth': 6,
            'color': '#8e8e93'
        }
    
    second_pointer = True if second_value is not None else False
    third_pointer = True if third_value is not None else False
    fourth_pointer = True if fourth_value is not None else False
    fifth_pointer = True if fifth_value is not None else False
    sixth_pointer = True if sixth_value is not None else False
    

    component_value = _component_func(value=value,second_value=second_value,third_value=third_value,fourth_value=fourth_value,fifth_value=fifth_value,sixth_value=sixth_value,
        second_pointer=second_pointer,third_pointer=third_pointer, fourth_pointer=fourth_pointer, fifth_pointer=fifth_pointer,sixth_pointer=sixth_pointer,
        min_value=min_value, max_value=max_value,title=title,title_fontsize=title_fontsize,title_color=title_color, key=key, customCSS=customCSS,
        id=id, width = width, height = height, valueFontColor = valueFontColor, valueFontFamily = valueFontFamily, symbol = symbol,minTxt = minTxt,maxTxt = maxTxt,
        reverse = reverse, textRenderer = textRenderer,gaugeWidthScale = gaugeWidthScale,gaugeColor = gaugeColor,label = label,labelFontColor = labelFontColor,
        shadowOpacity = shadowOpacity,shadowSize = shadowSize,shadowVerticalOffset = shadowVerticalOffset,levelColors = levelColors,startAnimationTime = startAnimationTime,
        startAnimationType = startAnimationType,refreshAnimationTime = refreshAnimationTime,refreshAnimationType = refreshAnimationType,
        donutStartAngle = donutStartAngle,valueMinFontSize = valueMinFontSize,labelMinFontSize = labelMinFontSize, minLabelMinFontSize = minLabelMinFontSize,
        maxLabelMinFontSize = maxLabelMinFontSize,hideValue = hideValue,hideMinMax = hideMinMax,
        showInnerShadow = showInnerShadow,humanFriendly = humanFriendly,noGradient = noGradient,
        donut = donut,differential = differential,relativeGaugeSize = relativeGaugeSize,counter = counter,decimals = decimals,customSectors = customSectors,formatNumber = formatNumber,
        pointer = pointer,pointerOptions = pointerOptions,second_pointerOptions=second_pointerOptions,third_pointerOptions=third_pointerOptions,fourth_pointerOptions=fourth_pointerOptions,
        fifth_pointerOptions=fifth_pointerOptions,sixth_pointerOptions=sixth_pointerOptions,displayRemaining = displayRemaining,
        imageDataEncoded=imageDataEncoded,tooltipPosition=tooltipPosition,enableTooltip=enableTooltip,tooltipText=tooltipText
    )
    
    return component_value
