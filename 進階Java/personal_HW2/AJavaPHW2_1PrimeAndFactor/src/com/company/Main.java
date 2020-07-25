package com.company;

import java.util.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) {
        //initialize...
        //scan
        Scanner input = new Scanner(System.in);
        //check
        String inputString;
        Optional<Integer> inputOptional;
        int inputInt;
        //containers
        List<Integer> factors, primeFactors;
        Map<Integer, Integer> primeFactorMaxPowers;
        //...initialize

        while(input.hasNext()){
            //get input & check
            inputOptional = Optional.empty();
            while(inputOptional.isEmpty()){
                inputString = input.next();
                inputOptional = stringToInt(inputString);
            }
            inputInt = inputOptional.get();

            //calculate required answers
            factors = getFactorList(inputInt);
            primeFactors = getPrimeList(factors);
            primeFactorMaxPowers = getMaxPowerMap(factors, primeFactors, inputInt);

            //output
            printIntegerList(factors);
            printIntegerList(primeFactors);
            printIntegerMap(primeFactorMaxPowers);
            System.out.println();
        }
    }
    public static Optional<Integer> stringToInt(String str){
        try{
            return Optional.of(Integer.parseInt(str));
        }catch(NumberFormatException e){
            System.out.println("Input must be an integer.");
            return Optional.empty();
        }
    }
    public static List<Integer> getFactorList(int n){
        return IntStream.rangeClosed(1, n).filter(x -> n % x == 0).boxed().collect(Collectors.toList());
    }
    public static List<Integer> getPrimeList(List<Integer> integerList){
        return integerList.stream().filter(Main::isPrime).collect(Collectors.toList());
    }
    public static boolean isPrime(int n){
        if(n == 1) return false;
        int root = (int)Math.sqrt(n);
        return IntStream.rangeClosed(2, root).takeWhile(x -> x <= root).noneMatch(x -> n % x == 0);
    }
    public static Map<Integer, Integer> getMaxPowerMap(List<Integer> factors, List<Integer> primeFactors, int n){
        Map<Integer, Integer> maxPowerMap = new HashMap<>();
        primeFactors.forEach(x -> {
            int maxPower = (int)IntStream.iterate(x, y -> y*x).limit(n).takeWhile(factors::contains).count();
            maxPowerMap.put(x, maxPower);
        });
        return maxPowerMap;
    }
    public static void printIntegerList(List<Integer> list){
        list.forEach(x -> {
            if(x.equals(list.get(0)))
                System.out.print(x);
            else
                System.out.print(" " + x);
        });
        System.out.println();
    }
    public static void printIntegerMap(Map<Integer, Integer> map){
        map.entrySet().stream().limit(1).forEach(x -> System.out.print("(" + x.getKey() + ", " + x.getValue() + ")"));
        map.entrySet().stream().skip(1).forEach(x -> System.out.print(" " + "(" + x.getKey() + ", " + x.getValue() + ")"));
        System.out.println();
    }
}
