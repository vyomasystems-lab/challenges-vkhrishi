module TrafficLights(light_M1,light_M2,light_MT,light_S,rst,clk,NO_of_vehical);
    
    
    input [4:0]NO_of_vehical;
    input rst;
    input clk;
    
    output [2:0] light_M1;
    reg [2:0] light_M1;
    output [2:0] light_M2;
    reg [2:0] light_M2;
    output [2:0] light_MT; 
    reg [2:0] light_MT;
    output [2:0] light_S;
    reg [2:0] light_S;

    parameter  S1=0, S2=1, S3 =2, S4=3, S5=4,S6=5;
    reg[3:0] count;
    reg[2:0] ps;
    

   
    
    always@( NO_of_vehical)
        begin
        if(rst==1)
        begin
        ps<=S2;
        
        end
        else
        
      
       
            
            case(ps)
                S1: if(NO_of_vehical== 7)
                        begin
                        ps<=S1;
                        
                        end
                    else
                        begin
                        ps<=S2;
                        
                        end
                S2: if(NO_of_vehical== 2)
                        begin
                        ps<=S2;
                        
                        end

                    else
                        begin
                        ps<=S3;
                       
                        end
                S3: if(NO_of_vehical== 5)
                        begin
                        ps<=S3;
                        
                        end

                    else
                        begin
                        ps<=S4;
                        
                        end
                S4:if(NO_of_vehical== 4)
                        begin
                        ps<=S4;
                        
                        end

                    else
                        begin
                        ps<=S5;
                        
                        end
                S5:if(NO_of_vehical== 3)
                        begin
                        ps<=S5;
                        
                        end

                    else
                        begin
                        ps<=S6;
                        
                        end

                S6:if(NO_of_vehical== 6)
                        begin
                        ps<=S6;
                        
                        end

                    else
                        begin
                        ps<=S1;
                        
                        end
                default: ps<=S1;
                endcase
            end   

            always@(ps)    
            begin
                
                case(ps)
                     
                    S1:
                    begin
                       light_M1<=3'b001;
                       light_M2<=3'b001;
                       light_MT<=3'b100;
                       light_S<=3'b100;
                    end
                    S2:
                    begin 
                       light_M1<=3'b001;
                       light_M2<=3'b010;
                       light_MT<=3'b100;
                       light_S<=3'b100;
                    end
                    S3:
                    begin
                       light_M1<=3'b001;
                       light_M2<=3'b100;
                       light_MT<=3'b001;
                       light_S<=3'b100;
                    end
                    S4:
                    begin
                       light_M1<=3'b010;
                       light_M2<=3'b100;
                       light_MT<=3'b010;
                       light_S<=3'b100;
                    end
                    S5:
                    begin
                       light_M1<=3'b100;
                       light_M2<=3'b100;
                       light_MT<=3'b100;
                       light_S<=3'b001;
                    end
                    S6:
                    begin 
                       light_M1<=3'b100;
                       light_M2<=3'b100;
                       light_MT<=3'b100;
                       light_S<=3'b010;
                    end
                    default:
                    begin 
                       light_M1<=3'b000;
                       light_M2<=3'b000;
                       light_MT<=3'b000;
                       light_S<=3'b000;
                    end
                    endcase
            end                
              

endmodule