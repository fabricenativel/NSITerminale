def mini(releve,date):
    indice_mini, temp_mini = 0, releve[0]
    for i in range(len(releve)):
        if releve[i]<temp_mini:
            indice_mini,temp_mini = i,releve[i]
    return temp_mini,date[indice_mini]