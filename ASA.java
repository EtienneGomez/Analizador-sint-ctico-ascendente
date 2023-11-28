import java.util.List;
import java.util.Stack;

public class ASA implements Parser{
    private int i = 0;
    private boolean hayErrores = false;
    private final List<Token> tokens;

    Object simb;

    Stack<Integer> estados = new Stack<>();
    

    public ASA(List<Token> tokens){
        this.tokens = tokens;
    }

    @Override
    public boolean parse() {
        estados.push(0);

        simb = tokens.get(i).tipo;

        while(!hayErrores){

            
            if(estados.peek() == 0){
                if(simb == "Q"){
                    estados.push(1);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.SELECT){
                    estados.push(2);
                    i++;
                    simb = tokens.get(i).tipo;
                } else
                    hayErrores = true;
            }
            else if(estados.peek() == 1){
                if(simb == TipoToken.EOF)
                    break;
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 2){
                if(simb == "D"){
                    estados.push(3);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.DISTINCT){
                    estados.push(4);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "P"){
                    estados.push(5);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.ASTERISCO){
                    estados.push(6);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "A"){
                    estados.push(7);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "A2"){
                    estados.push(8);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.IDENTIFICADOR){
                    estados.push(9);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 3){
                if(simb == TipoToken.FROM){
                    estados.push(17);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 4){
                if(simb == TipoToken.ASTERISCO){
                    estados.push(6);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "A"){
                    estados.push(7);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "A2"){
                    estados.push(8);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.IDENTIFICADOR){
                    estados.push(9);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "P"){
                    estados.push(10);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 5){
                if(simb == TipoToken.FROM){
                    simb = "D";
                    i--;
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 6){
                if(simb == TipoToken.FROM){
                    simb = "P";
                    i--;
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 7){
                if(simb == TipoToken.FROM){
                    simb = "P";
                    i--;
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 8){
                if(simb == TipoToken.FROM){
                    simb = "A1";
                    i--;
                }
                
                else if(simb == "A1"){
                    estados.push(11);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.COMA){
                    estados.push(12);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 9){
                if(simb == TipoToken.FROM){
                    simb = "A3";
                    i--;
                }
                else if(simb == TipoToken.COMA){
                    simb = "A3";
                    i--;
                }
                else if(simb == "A3"){
                    estados.push(13);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.PUNTO){
                    estados.push(14);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 10){
                if(simb == TipoToken.FROM){
                    simb = "D";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if (estados.peek() == 11){
                if(simb == TipoToken.FROM){
                    simb = "A";
                    i--;
                    estados.pop();
                    estados.pop();
                } else
                    hayErrores = true;
            }
            else if(estados.peek() == 12){
                if(simb == "A2"){
                    estados.push(8);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.IDENTIFICADOR){
                    estados.push(9);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "A"){
                    estados.push(15);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 13){
                if(simb == TipoToken.FROM){
                    simb = "A2";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else if(simb == TipoToken.COMA){
                    simb = "A2";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else
                    hayErrores = true;
            }else if(estados.peek() == 14){
                if(simb == TipoToken.IDENTIFICADOR){
                    estados.push(16);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 15){
                if(simb == TipoToken.FROM){
                    simb = "A1";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 16){
                if(simb == TipoToken.FROM){
                    simb = "A3";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else if(simb == TipoToken.COMA){
                    simb = "A3";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 17){
                if(simb == "T2"){
                    estados.push(18);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.IDENTIFICADOR){
                    estados.push(20);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "T"){
                    estados.push(25);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 18){
                if(simb == "T1"){
                    estados.push(19);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.COMA){
                    estados.push(21);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.EOF){
                    simb = "T1";
                    i--;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 19){
                if(simb == TipoToken.EOF){
                    simb = "T";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 20){
                if(simb == "T3"){
                    estados.push(23);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.IDENTIFICADOR){
                    estados.push(24);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.COMA){
                    simb = "T3";
                    i--;
                }
                else if(simb == TipoToken.EOF){
                    simb = "T3";
                    i--;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 21){
                if(simb == "T2"){
                    estados.push(18);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == TipoToken.IDENTIFICADOR){
                    estados.push(20);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else if(simb == "T"){
                    estados.push(22);
                    i++;
                    simb = tokens.get(i).tipo;
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 22){
                if(simb == TipoToken.EOF){
                    simb = "T1";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 23){
                if(simb == TipoToken.COMA){
                    simb = "T2";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else if(simb == TipoToken.EOF){
                    simb = "T2";
                    i--;
                    estados.pop();
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 24){
                if(simb == TipoToken.COMA){
                    simb = "T3";
                    i--;
                    estados.pop();
                }
                else if(simb == TipoToken.EOF){
                    simb = "T3";
                    i--;
                    estados.pop();
                }
                else
                    hayErrores = true;
            }
            else if(estados.peek() == 25){
                if(simb == TipoToken.EOF){
                    simb = "Q";
                    i--;
                    estados.pop();
                    estados.pop();
                    estados.pop();
                    estados.pop();
                }
                else
                    hayErrores = true;
            }

            
        }
        if(hayErrores){
            System.out.println("La Consulta es INCORRECTA");
            return false;
        }
        else{
            System.out.println("La sintaxis es CORRECTA");
            return true;
        }
    }
}
