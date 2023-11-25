package main.java.personal;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;



public class Div {
    
    public Div(){

    }

    //---------------------------------- Validator ----------------------------------
    public boolean kunBokstaver(String tekst){
        return tekst.matches("[a-zA-ZæøåÆØÅ\s]+"); // \s inkluderer mellomrom
    }

    //---------------------------------- Nice print ----------------------------------
    private void print(String message) {
        String identification = String.format("[%s] ", this.getClass().getSimpleName());   
        System.out.println(identification.concat(message));
    }

    //---------------------------------- Diverse jeg vil ta vare på ----------------------------------
    public int dice(){
        return (int)(Math.random() * 6 +1);
    }

    public void streamsMetoder(){

        Collection<String> liste = new ArrayList<>(Arrays.asList("S", "t", "r", "e", "a", "m"));

        print(Long.toString( liste.stream().filter(m-> m.equals("S")).count() ));     // 1
        liste = liste.stream().map(character -> character.concat("ee")).collect(Collectors.toList());  // [See, tee, ree, eee, aee, mee]
    }

    public void ifMethod(){
        //(List.iterator().hasNext() ? new Object(arg, List.iterator().next()) : null)
        boolean check = true;
        String string = ( check ? "True" : "False");
        print(string);
    }

    public void shufflePerfectly(List<String> list){
        //Splitter først stokken
        int half = list.size()/2;
        List<String> første = list.subList(0, half);
        List<String> andre = list.subList(half, list.size());
        
        //Stokker:
        ArrayList<String> shuffled = new ArrayList<>();
        for (int i = 0; i < list.size(); i++) {
            if (i%2==0) {
                shuffled.add(første.get(i/2));
            } else if (i%2==1){
                shuffled.add(andre.get(i/2));
            }
        }
        print(shuffled.toString());
    }


    //---------------------------------- main for testing/running ----------------------------------
    public static void main(String[] args) {
        Div testing = new Div();
        testing.ifMethod();
    }
}
