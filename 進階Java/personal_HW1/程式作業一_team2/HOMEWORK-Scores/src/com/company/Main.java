package com.company;

import javax.swing.*;

import static java.util.Comparator.comparing;
import static java.util.Comparator.comparingDouble;
import static java.util.stream.Collectors.*;
//import static java.util.stream.Collectors.toList;
import java.util.*;
import java.util.stream.*;
import java.io.*;

import java.text.ParseException;

import java.util.DoubleSummaryStatistics;

public class Main {
    public static void main(String[] args) throws Exception  {
	    // DATA INPUT
        /*
            This Section Is Only For Extracting Data From File
            Q1 to Q8 below this section only used Streams, Lambdas, and Method Reference
        */
        // DATA INPUT
        List<Student> students = new ArrayList<>();
        Scanner scanner = new Scanner(new File("DATA.csv"));

        while (scanner.hasNextLine())  //returns a boolean value
        {
            //FN-LN-LOC-DATE-GENDER-MATH-ENGLISH-CHINESE-AVERAGE-ID
            String buffer = scanner.nextLine();
            Scanner lineScanner = new Scanner(buffer);
            lineScanner.useDelimiter(",");
            Student input = new Student();

            input.Info.FirstName = lineScanner.next();
            input.Info.LastName = lineScanner.next();
            input.Info.city = City.fromId(Integer.parseInt(lineScanner.next()));
            input.Info.BirthDay = lineScanner.next();
            input.Info.gender = Gender.fromId(Integer.parseInt(lineScanner.next()));

            input.Scores.Math = Integer.parseInt(lineScanner.next());
            input.Scores.English = Integer.parseInt(lineScanner.next());
            input.Scores.Chinese = Integer.parseInt(lineScanner.next());
            input.Scores.Average = Double.parseDouble(lineScanner.next());

            input.Id = lineScanner.next();

            lineScanner.close();
            students.add(input);
        }
        scanner.close();  //closes the scanner

        Scanner input = new Scanner(System.in);
        String inputString = "-1";

        while(!inputString.equals("0"))
        {
            System.out.println("Please enter the question's number(1~8, 0 = exit) : ");
            inputString = input.next();
            switch(inputString)
            {
                case "0":  //Exit
                    break;

                case "1":  //Q1

                    //List result = students.stream().sorted(comparing(Student::getId)).collect(toList());
                    Stream<Student> Q1OutputA = students.stream().sorted(comparing(Student::getId)),
                                    Q1OutputB = students.stream().sorted((o1, o2) -> {
                                        try {
                                            return o2.getDate().compareTo(o1.getDate());
                                        } catch (ParseException e) {
                                            System.out.println("Date Converter Error");
                                        }
                                        return 0;
                                    });

                    System.out.println("Q1(1) : ");
                    Q1OutputA.forEach(student -> System.out.println(student.getInfo().getFirstName() + " " + student.getInfo().getLastName()));
                    System.out.println();

                    System.out.println("Q1(2) : ");
                    Q1OutputB.forEach(student -> System.out.println(student.getInfo().getFirstName() + " " + student.getInfo().getLastName()));
                    System.out.println();

                    break;

                case "2":  //Q2

                    System.out.println("Q2 : ");

                    Set<Person> Q2Persons = students.stream().map(Student::getInfo).collect(Collectors.toSet());
                    Set<City> Q2City = Q2Persons.stream().map(Person::getCity).collect(Collectors.toSet());
                    Set<String> Q2Output = Q2City.stream().map(City::getIDString).collect(Collectors.toSet());

                    Q2Output.forEach(System.out::println);
                    System.out.println();

                    break;

                case "3":  //Q3

                    System.out.println("Q3 : ");

                    Map<String, List<Person>> Q3Output = students.stream().map(Student::getInfo).collect(Collectors.groupingBy(Person -> Person.city.getIDString()));

                    Q3Output.forEach((name, list) -> {
                        System.out.println(name + ":");
                        list.forEach(Person -> System.out.println(Person.getFirstName() + " " + Person.getLastName()));
                        System.out.println();
                    });

                    break;

                case "4":  //Q4

                    System.out.println("Q4 : ");

                    Map<Boolean, List<Person>> Q4Output = students.stream().map(Student::getInfo).collect(partitioningBy(Person -> Person.gender.getId() == 0));

                    Q4Output.forEach((gender, list) -> {
                        System.out.println(gender ? "Male:" : "Female:");
                        list.forEach(Person -> System.out.println(Person.getFirstName() + " " + Person.getLastName()));
                        System.out.println();
                    });

                    break;

                case "5":  //Q5

                    System.out.println("Q5 : ");

                    DoubleSummaryStatistics Q5OutputMathInfo = students.stream().map(Student::getScores).collect(summarizingDouble(ScoreSheet::getMath)),
                                            Q5OutputEnglishInfo = students.stream().map(Student::getScores).collect(summarizingDouble(ScoreSheet::getEnglish)),
                                            Q5OutputChineseInfo = students.stream().map(Student::getScores).collect(summarizingDouble(ScoreSheet::getChinese));

                    System.out.println("Math:\n" +
                            "\tAverage:\t" + Q5OutputMathInfo.getAverage() + "\n" +
                            "\tMinimum:\t" + Q5OutputMathInfo.getMin() + "\n" +
                            "\tMaximum:\t" + Q5OutputMathInfo.getMax() + "\n");
                    System.out.println("English:\n" +
                            "\tAverage:\t" + Q5OutputEnglishInfo.getAverage() + "\n" +
                            "\tMinimum:\t" + Q5OutputEnglishInfo.getMin() + "\n" +
                            "\tMaximum:\t" + Q5OutputEnglishInfo.getMax() + "\n");
                    System.out.println("Chinese:\n" +
                            "\tAverage:\t" + Q5OutputChineseInfo.getAverage() + "\n" +
                            "\tMinimum:\t" + Q5OutputChineseInfo.getMin() + "\n" +
                            "\tMaximum:\t" + Q5OutputChineseInfo.getMax() + "\n");

                    break;

                case "6":  //Q6

                    System.out.println("Q6 : ");

                    Set<Student>    Q6OutputMath = students.stream().filter(student -> student.getScores().getMath() >= 60).collect(Collectors.toSet()),
                                    Q6OutputEnglish = students.stream().filter(student -> student.getScores().getEnglish() >= 60).collect(Collectors.toSet()),
                                    Q6OutputChinese = students.stream().filter(student -> student.getScores().getChinese() >= 60).collect(Collectors.toSet());

                    System.out.println("Students who failed Math : ");
                    Q6OutputMath.forEach(student -> System.out.println(student.getId() + " " + student.getInfo().getFirstName() + " " + student.getInfo().getLastName()));
                    System.out.println();
                    System.out.println("Students who failed English : ");
                    Q6OutputEnglish.forEach(student -> System.out.println(student.getId() + " " + student.getInfo().getFirstName() + " " + student.getInfo().getLastName()));
                    System.out.println();
                    System.out.println("Students who failed Chinese : ");
                    Q6OutputChinese.forEach(student -> System.out.println(student.getId() + " " + student.getInfo().getFirstName() + " " + student.getInfo().getLastName()));
                    System.out.println();

                    break;

                case "7":  //Q7

                    System.out.println("Q7 : ");

                    Stream<Student> Q7Output = students.stream().sorted((o1, o2) -> Double.compare(o2.getScores().getAverage(), o1.getScores().getAverage()));

                    Q7Output.forEach(student -> System.out.println(student.getId() + ", " +
                            student.getInfo().getFirstName() + " " + student.getInfo().getLastName() + ", " +
                            student.getScores().getAverage()));
                    System.out.println();

                    break;

                case "8":  //Q8

                    System.out.println("Q8 : ");

                    Map<Boolean, List<Student>> Q8OutputMath = students.stream().collect(partitioningBy(Student -> Student.getScores().getMath() >= 60)),
                            Q8OutputEnglish = students.stream().collect(partitioningBy(Student -> Student.getScores().getEnglish() >= 60)),
                            Q8OutputChinese = students.stream().collect(partitioningBy(Student -> Student.getScores().getChinese() >= 60));

                    Q8OutputMath.forEach((passed, list) -> {
                        System.out.println(passed ? "Math score >= 60 : " : "Math score < 60 : ");
                        list.forEach(Student -> System.out.println(Student.getInfo().getFirstName() + " " + Student.getInfo().getLastName()));
                        System.out.println();
                    });
                    Q8OutputEnglish.forEach((passed, list) -> {
                        System.out.println(passed ? "English score >= 60 : " : "English score < 60 : ");
                        list.forEach(Student -> System.out.println(Student.getInfo().getFirstName() + " " + Student.getInfo().getLastName()));
                        System.out.println();
                    });
                    Q8OutputMath.forEach((passed, list) -> {
                        System.out.println(passed ? "Chinese score >= 60 : " : "Chinese score < 60 : ");
                        list.forEach(Student -> System.out.println(Student.getInfo().getFirstName() + " " + Student.getInfo().getLastName()));
                        System.out.println();
                    });

                    break;

                default:
                    System.out.println("Input must be an integer between 1 and 8.");
            }
        }

    }
    
}
