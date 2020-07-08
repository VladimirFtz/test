from datetime import datetime
import time

start_time = datetime.now()

end_time = datetime.now()
exec_time = (end_time - start_time)
print('Finished!')
print('start_time: ', start_time)
print('end_time: ', end_time)
print('exec_time: ', exec_time) 