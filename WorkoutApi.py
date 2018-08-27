import requests

API_URL = 'https://api.netpulse.com/np/workouts-partner/v1.0/'

class ServerApi():

    # display workouts by exceciserUuid
    def workoutByExceciserUuid (self, token, uuid, categoryId, modifiedAt, limit, page):

        headers = {'content-type': 'application/json', 'access_token': token, }
        r = requests.get(API_URL + 'exercisers/'
                + str(uuid) + '/workouts?'
                + 'categoryId=' + str(categoryId)
                + '&modifiedAt=' + str(modifiedAt)
                + '&page=' + str(page)
                + '&limit=' + str(limit), headers=headers)
        return r

    # display workouts by workoutId
    def workoutByWorkoutId (self, token, workoutId):

        headers = {'content-type': 'application/json', 'access_token': token, }
        r = requests.get(API_URL + 'workouts/' + str(workoutId), headers=headers)
        return r