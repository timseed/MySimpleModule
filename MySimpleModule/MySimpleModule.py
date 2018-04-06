class MySimpleModule(object):

    def __init__(self):
        self.dummy_data=[1,2,3]

    def isInData(self,n):
        """
        Is the supplied number in the self.data list
        :param n:
        :return: True or False
        """
        try:
            if n in self.dummy_data:
                return True
            else:
                return False
        except Exception as err:
            raise ValueError
