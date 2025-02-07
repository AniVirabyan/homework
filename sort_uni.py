
class University:
    def __init__(self, name, year, students):
        self.name = name
        self.year = int(year)
        self.students = int(students)

    def __str__(self):
        return f"{self.name} (Founded: {self.year}, Students: {self.students})"

    def read_university(self, fname):
        universities = []
        with open(fname, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    university = University(parts[0], parts[1], parts[2])
                    universities.append(university)
        return universities

    def save_sorted_universities(self, universities, output_fname):
        with open(output_fname, "w", encoding="utf-8") as file:
            for uni in universities:
                file.write(f"{uni.name},{uni.year},{uni.students}\n")


def sort_by_year(university):
    return university.year


def main():
    input_fname = "university.txt"  
    output_fname = "sorted_universities.txt"  

    uni = University("", 0, 0)
    universities = uni.read_university(input_fname)

   
    universities.sort(key=sort_by_year)

    
    uni.save_sorted_universities(universities, output_fname)

    print(f"Universities sorted and saved to {output_fname}.")


if __name__ == "__main__":
    main()

