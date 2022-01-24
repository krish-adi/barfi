class Link(object):
    """

    """

    def __init__(self, **kwargs):
        # Initialise the Link object

        # To set the name of the Link, default = Link
        self.LinkName = kwargs.get('name', 'Link')

        # To set the defaults for LinkData
        self.LinkData = {}
        