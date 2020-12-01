#!/usr/bin/python -t

'''
Definition of PushNotification
class PushNotification:
    @classmethod
    def notify(user_id, message):
'''
class PubSubPattern:
    def __init__(self):
    # do intialization if necessary
        self.d = {}

        return
    
    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """
    def subscribe(self, channel, user_id):
        # write your code here
        if channel not in self.d:
            self.d[channel] = set()
        
        self.d[channel].add(user_id)

    """
    @param: channel: a channel name
    @param: user_id: a user id
    @return: nothing
    """

    def unsubscribe(self, channel, user_id):
    	# write your code here
    	if channel not in self.d:
    	    return
        if user_id not in self.d[channel]:
            return
        
        self.d[channel].remove(user_id)
        if len(self.d[channel]) == 0:
            del self.d[channel]
        
        return
        
    """
    @param: channel: a channel name
    @param: message: need send message
    @return: nothing
    """

    def publish(self, channel, message):
		# write your code here
		if channel not in self.d:
		    return
		
		for user in self.d[channel]:
		    PushNotification.notify(user, message)
		    
		return
		
