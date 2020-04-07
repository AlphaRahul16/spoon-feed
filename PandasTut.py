
from locust import TaskSet, task, HttpLocust
import random
import pandas
result = pandas.read_csv('/Users/rahul/Desktop/standOrder.csv')
print(result.shape)

department = "a2783da8f319d3e795adf0f260ba83e9d35a14d4f3e35082082730371a0ff1b1";
headers = {
    'accept': 'application/json',
    'authorization': 'Basic dGVzdHVzZXI6dGVzdHBhc3M=',
    'Content-Type': 'application/json'
}

class MyTaskSet(TaskSet):

    @task
    def task1(self):
        for i in range(len(result)):
            orderGUID = result.loc[i, "UUID"]
            orderNum = result.loc[i, "OrderNumber"]
            print(orderGUID,orderNum)
            response = self.client.get("/department/" + department + "/standard_order/"+orderGUID+"",headers=headers)
            print(response)
            assert orderNum in response.text

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000








# env = gym.make("MountainCar-v0")
# env.reset()
# LEARNING_RATE = 0.1
# DISCOUNT = 0.95
# EPISODES = 25000
#
#
# DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
# discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE
#
# q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))
#
# '''done = False
#
# while not done:
#     action = 2
#     new_state, reward, done, _ = env.step(action)
#     env.render()
#
# env.close()'''

