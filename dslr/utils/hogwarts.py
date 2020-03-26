def generate_hogwarts_house_mask(df=None):
    isGryffindor = df["Hogwarts House"] == "Gryffindor"
    isSlytherin = df["Hogwarts House"] == "Slytherin"
    isRavenclaw = df["Hogwarts House"] == "Ravenclaw"
    isHufflepuff = df["Hogwarts House"] == "Hufflepuff"

    return [isGryffindor, isSlytherin, isHufflepuff, isRavenclaw]
