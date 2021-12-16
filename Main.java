import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Main {


    public static void main(String[] args) {
        try {
            File myObj = new File("values.txt");
            ArrayList<Integer> numbers = new ArrayList<>();
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                int data = Integer.parseInt(myReader.nextLine().trim());
                numbers.add(data);
            }
            myReader.close();
            int suma;
            int sumaAnterior =0;
            int veg=0;
            for(int i = 0; i < numbers.size()-2; i++){
                suma =0;
                for (int x =0; x< 3;x++){
                    suma+= numbers.get(i+x);
                }
                if (suma > sumaAnterior){
                    veg++;
                }
                sumaAnterior = suma;
            }
            System.out.println(veg);
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
