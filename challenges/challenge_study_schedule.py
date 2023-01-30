def study_schedule(permanence_period, target_time):

    studants_Online = 0
    try:
        for entry, exits in permanence_period:
            if entry <= target_time <= exits:
                studants_Online += 1
        return studants_Online
    except TypeError:
        return None
