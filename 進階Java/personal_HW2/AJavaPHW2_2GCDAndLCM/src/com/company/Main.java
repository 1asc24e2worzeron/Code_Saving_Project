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
        int n1, n2;
        boolean pass1, pass2;

        //input / output list
        List<Map.Entry<Integer, Integer>> inputMapList = new ArrayList<>(), GCDAndLCMList = new ArrayList<>();
        //...initialize

        //get & check & save inputs
        while(input.hasNext()){
            pass1 = false;
            pass2 = false;
            n1 = -1;
            n2 = -1;
            while(!pass2){
                inputOptional = Optional.empty();
                while (inputOptional.isEmpty()) {
                    inputString = input.next();
                    inputOptional = stringToInt(inputString);
                }
                if(!pass1){
                    n1 = inputOptional.get();
                    pass1 = true;
                }
                else{
                    n2 = inputOptional.get();
                    pass2 = true;
                }
            }
            inputMapList.add(Map.entry(n1, n2));
        }

        //calculate required answers & save & output
        if(!inputMapList.isEmpty()) {
            inputMapList.stream().forEach(x -> GCDAndLCMList.add(getGCDAndLCM(x)));
            GCDAndLCMList.forEach(GCDAndLCM -> System.out.println(GCDAndLCM.getKey() + " " + GCDAndLCM.getValue()));
        }
    }
    public static Optional<Integer> stringToInt(String str){
        try{
            if(str.equals("0"))
                throw new NumberFormatException();
            return Optional.of(Integer.parseInt(str));
        }catch(NumberFormatException e){
            System.out.println("Input must be an non-zero integer.");
            return Optional.empty();
        }
    }
    public static Map.Entry<Integer, Integer> getGCDAndLCM(Map.Entry<Integer, Integer> source){
        int gcd =
                Stream.iterate(source, x -> x.getKey() != 0, x -> {
                    int n1 = x.getValue(), n2 = x.getValue() != 0 ? x.getKey() % x.getValue() : 0;
                    return Map.entry(n1, n2);
                }).filter(x -> x.getValue() == 0).collect(Collectors.toList()).get(0).getKey();
        int lcm = Math.abs(source.getKey()*source.getValue())/gcd;
        return Map.entry(gcd, lcm);
    }
}
