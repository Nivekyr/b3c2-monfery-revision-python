def compte_mots(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

def ecrire_resultat(filename, count):
    with open(filename, 'w') as file:
        file.write(f"Nombre de mots: {count}")

def main():
    input_file = "exo7.txt"
    output_file = "resultat.txt"
    count = compte_mots(input_file)
    ecrire_resultat(output_file, count)
    print(count)

main()