import logging
logging.basicConfig(level=logging.INFO)
from .abstract_clockify import AbstractClockify
from .user import User
# Represents time spent on a Task by a User 
class TimeEntry(AbstractClockify):
    
    def __init__(self,api_key):
        super(TimeEntry,self).__init__(api_key=api_key)
	
	# returns all time entry
    def get_all_time_entry_user(self,workspace_id,user_id): 
        try:
            logging.info("Start function: get_all_time_entry_user")
            url = self.base_url+'v1/workspaces/'+workspace_id+'/user/'+user_id+'/time-entries'
            r = self.request_get(url)
            time_entries = []
            time_entries.append(r)
            has_time_entry = True
            page = 1
            while (has_time_entry):
                urlx = url + "/?page="+str(page)
                r = self.request_get(urlx)
                if len(r) > 0:
                    time_entries.append(r)
                    page = page + 1
                elif len(r) < 50 or len(r) == 0:
                    has_time_entry = False
                    page = 1     
            
            time_entries_list = []
            for time_entry in time_entries:
                for te in time_entry:
                    time_entries_list.append (te)
            return time_entries_list	
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__)

    def get_by_workspace_function(self, workspace, **kwargs):
        result = []
        time_entries = []
        
        try:
            function = kwargs["function"]

            logging.info("Start function: get_by_workspace_function")

            users = User.get_all_workspace_users(self,workspace['id'])
            for user in users:
                user_id = user['id']
                result = self.get_all_time_entry_user(workspace['id'], user_id)
                for entry in result:
                    value = entry
                    time_entries.append(value)
                    if function is not None:
                        function (data=value, topic=kwargs["topic"], extra_data=kwargs["extra_data"])
				
        except Exception as e: 
            logging.error("OS error: {0}".format(e))
            logging.error(e.__dict__) 

        logging.info("Retrieve All Time Entries")
        return time_entries

