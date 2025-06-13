SERVICES = {
        # Name                              namespace                           wsdl file                      binding name
        'devicemgmt'   : {'ns': 'http://www.onvif.org/ver10/device/wsdl',    'wsdl': 'ver10/device/wsdl/devicemgmt.wsdl', 'binding' : 'DeviceBinding'},
        'media'        : {'ns': 'http://www.onvif.org/ver10/media/wsdl',     'wsdl': 'ver10/media/wsdl/media.wsdl',      'binding' : 'MediaBinding'},
        'ptz'          : {'ns': 'http://www.onvif.org/ver20/ptz/wsdl',       'wsdl': 'ver20/ptz/wsdl/ptz.wsdl',        'binding' : 'PTZBinding'},
        'imaging'      : {'ns': 'http://www.onvif.org/ver20/imaging/wsdl',   'wsdl': 'ver20/imaging/wsdl/imaging.wsdl',    'binding' : 'ImagingBinding'},
        'deviceio'     : {'ns': 'http://www.onvif.org/ver10/deviceIO/wsdl',  'wsdl': 'ver10/deviceIO/wsdl/deviceio.wsdl',   'binding' : 'DeviceIOBinding'},
        'events'       : {'ns': 'http://www.onvif.org/ver10/events/wsdl',    'wsdl': 'ver10/events/wsdl/events.wsdl',     'binding' : 'EventBinding'},
        'pullpoint'    : {'ns': 'http://www.onvif.org/ver10/events/wsdl',    'wsdl': 'ver10/events/wsdl/events.wsdl',     'binding' : 'PullPointSubscriptionBinding'},
        'notification' : {'ns': 'http://www.onvif.org/ver10/events/wsdl',    'wsdl': 'ver10/events/wsdl/events.wsdl',     'binding' : 'NotificationProducerBinding'},
        'subscription' : {'ns': 'http://www.onvif.org/ver10/events/wsdl',    'wsdl': 'ver10/events/wsdl/events.wsdl',     'binding' : 'SubscriptionManagerBinding'},
        'analytics'    : {'ns': 'http://www.onvif.org/ver20/analytics/wsdl', 'wsdl': 'ver20/analytics/wsdl/analytics.wsdl',  'binding' : 'AnalyticsEngineBinding'},
        'recording'    : {'ns': 'http://www.onvif.org/ver10/recording/wsdl', 'wsdl': 'ver10/recording/wsdl/recording.wsdl',  'binding' : 'RecordingBinding'},
        'search'       : {'ns': 'http://www.onvif.org/ver10/search/wsdl',    'wsdl': 'ver10/search/wsdl/search.wsdl',     'binding' : 'SearchBinding'},
        'replay'       : {'ns': 'http://www.onvif.org/ver10/replay/wsdl',    'wsdl': 'ver10/replay/wsdl/replay.wsdl',     'binding' : 'ReplayBinding'},
        'receiver'     : {'ns': 'http://www.onvif.org/ver10/receiver/wsdl',  'wsdl': 'ver10/receiver/wsdl/receiver.wsdl',   'binding' : 'ReceiverBinding'},
        }

#
#NSMAP = { }
#for name, item in SERVICES.items():
#    NSMAP[item['ns']] = name
