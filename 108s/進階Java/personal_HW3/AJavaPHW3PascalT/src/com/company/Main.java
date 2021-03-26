package com.company;

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;
import java.util.stream.Collector;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) {
        int n;
        Scanner input = new Scanner(System.in);

        while(input.hasNext()) {
            n = input.nextInt();
            printPascalTriangle(n);
        }
    }
    public static void printPascalTriangle(int n){
        Deque<Integer> pascalLines = new ArrayDeque<>();
        pascalLines.offerFirst(1);

        Stream.iterate(pascalLines, line -> {
            Deque<Integer> regPascalLine = new ArrayDeque<>(), newPascalLine = new ArrayDeque<>();
            line.forEach(x -> regPascalLine.offerFirst(x));
            line.offerFirst(0);
            regPascalLine.offerLast(0);

            Stream.iterate(line, x -> x).limit(line.size()).forEach(x -> {
                newPascalLine.offerFirst(x.pollFirst().intValue() + regPascalLine.pollFirst().intValue());
            });
            return newPascalLine;
        }).limit(n + 1).forEach(line -> {
            Stream.iterate(0, x -> x < n + 1 - line.size(), x -> x + 1).forEach(x -> System.out.print(" "));
            line.forEach(x -> System.out.print(x + " "));
            System.out.println();
        });
    }
}
