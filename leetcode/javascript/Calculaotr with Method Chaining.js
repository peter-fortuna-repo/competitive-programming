// Link to problem: https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator {
    
    /** 
     * @param {number} value
     */
    constructor(value) {
        this.result = value;
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    add(value){
        return new Calculator(this.result + value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    subtract(value){
        return new Calculator(this.result - value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */  
    multiply(value) {
        return new Calculator(this.result * value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    divide(value) {
        if(value == 0){
            throw "Division by zero is not allowed";
        }
        return new Calculator(this.result / value);
    }
    
    /** 
     * @param {number} value
     * @return {Calculator}
     */
    power(value) {
        return new Calculator(this.result ** value);
    }
    
    /** 
     * @return {number}
     */
    getResult() {
        return this.result;       
    }
}