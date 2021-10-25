// level is in range [0, 2]
// Summation/Subtraction - kind = 0
// 0 - 1 sign 1, sign: +/-
// 1 - 10 sign 1, sign: +/-
// 2 - 100 sign 1, sign: +/-
// 3 - 10 sign 10, sign: +/-
// 4 - 10 sign 100, sign: +/-
// 5 - 100 sign 100, sign: +/-

// Multiplication - kind = 1
// 6 - 1 sign 1, sign: *
// 7 - 1 sign 10, sign *
// 8 - 1 sign 100, sign *
// 9 - 10 sign 10, sign *
// 10 - 10 sign 100, sign *
// 11 - 100 sign 100, sign *


// (0, 0) -> (0, 1) -> ()

// Complex
// 12 - (1 sign 1) 1, sign +/-
// 13 - (1 sign 10) 1 | (10 sign 1) 1, sign +/-
// 14 - ()


// max - 18

const levels_conf = {
  level1 : {
    num_vars: 2,
    vars: {
        n1_start: 1,
        n2_start: 1,
        n1_end: 10,
        n2_end: 10,
        sign: 0
    }
  },

// max - 98
level2 : {
    num_vars: 2,
    vars: {
        n1_start: 10,
        n2_start: 10,
        n1_end: 50,
        n2_end: 50,
        sign: 0
    }
},

// mx - 72
level3 : {
    num_vars: 2,
    vars: {
        n1_start: 1,
        n2_start: 1,
        n1_end: 10,
        n2_end: 10,
        sign: 1
    }
},

// max - 162
level4 : {
    num_vars: 3,
    vars: {
        n1_start: 1,
        n2_start: 1,
        n3_start: 1,
        n1_end: 10,
        n2_end: 10,
        n3_end: 10,
    }
},

// max - 361
level5 : {
    num_vars: 2,
    vars: {
        n1_start: 10,
        n2_start: 10,
        n1_end: 20,
        n2_end: 20,
        sign: 1
    }
},

// max - 500
level6 : {
    num_vars: 2,
    vars: {
        n1_start: 100,
        n2_start: 100,
        n1_end: 250,
        n2_end: 250,
        sign: 0
    }
},

// max - 702
level7 : {
    num_vars: 3,
    vars: {
        n1_start: 20,
        n2_start: 20,
        n3_start: 1,
        n1_end: 40,
        n2_end: 40,
        n3_end: 10,
    }
},

// max - 1000
level8 : {
    num_vars: 2,
    vars: {
        n1_start: 250,
        n2_start: 250,
        n1_end: 500,
        n2_end: 500,
        sign: 0
    }
},

// max - 1521
level9 : {
    num_vars: 2,
    vars: {
        n1_start: 10,
        n2_start: 10,
        n1_end: 40,
        n2_end: 40,
        sign: 1
    }
},

// max - 1782
level10 : {
    num_vars: 3,
    vars: {
        n1_start: 1,
        n2_start: 1,
        n3_start: 10,
        n1_end: 10,
        n2_end: 10,
        n3_end: 100,
    }
},

// max - 1998
level11 : {
    num_vars: 2,
    vars: {
        n1_start: 500,
        n2_start: 500,
        n1_end: 1000,
        n2_end: 1000,
        sign: 0
    }
},

// max - 2352
level12 : {
    num_vars: 3,
    vars: {
        n1_start: 10,
        n2_start: 10,
        n3_start: 25,
        n1_end: 25,
        n2_end: 25,
        n3_end: 50,
    }
},

// max - 3498
level13 : {
    num_vars: 2,
    vars: {
        n1_start: 1000,
        n2_start: 1000,
        n1_end: 1750,
        n2_end: 1750,
        sign: 0
    }
},

// max - 4761
level14 : {
    num_vars: 2,
    vars: {
        n1_start: 40,
        n2_start: 40,
        n1_end: 70,
        n2_end: 70,
        sign: 1
    }
},

// max - 5782
level15 : {
    num_vars: 3,
    vars: {
        n1_start: 25,
        n2_start: 25,
        n3_start: 25,
        n1_end: 60,
        n2_end: 60,
        n3_end: 50,
    }
},


// max - 6998
level16 : {
    num_vars: 2,
    vars: {
        n1_start: 1750,
        n2_start: 1750,
        n1_end: 3500,
        n2_end: 3500,
        sign: 0
    }
},

// max - 7921
level17 : {
    num_vars: 2,
    vars: {
        n1_start: 70,
        n2_start: 70,
        n1_end: 90,
        n2_end: 90,
        sign: 1
    }
},

// max - 9702
level18 : {
    num_vars: 3,
    vars: {
        n1_start: 50,
        n2_start: 50,
        n3_start: 30,
        n1_end: 100,
        n2_end: 100,
        n3_end: 50,
    }
},

// max - 9998
level19 : {
    num_vars: 2,
    vars: {
        n1_start: 3500,
        n2_start: 3500,
        n1_end: 5000,
        n2_end: 5000,
        sign: 0
    }
},

// max - 11881
level20 : {
    num_vars: 2,
    vars: {
        n1_start: 90,
        n2_start: 90,
        n1_end: 110,
        n2_end: 110,
        sign: 1
    }
},

// max - 14652
level21 : {
    num_vars: 3,
    vars: {
        n1_start: 50,
        n2_start: 50,
        n3_start: 50,
        n1_end: 75,
        n2_end: 75,
        n3_end: 100,
    }
}



}

export {generateQuestion2, levels_conf, generateQuestion, getRandomInt}

// eslint-disable-next-line no-unused-vars
function generateQuestion2(kind, level){
    let sign = ""
    if (kind === 0){
        let sign_choice = getRandomInt(0, 2)
        if (sign_choice === 0){
            sign = "+"
        }else{
            sign = "-"
        }
    }else{
        sign = "*"
    }


    let num1 = 0
    let num2 = 0
    let choice = getRandomInt(0, 2)
    if (level % 6 === 0){
        num1 = getRandomInt(1, 10)
        num2 = getRandomInt(1, 10)
    }
    else if (level % 6 === 1){
        if (choice ===  0){
            num1 = getRandomInt(10, 100)
            num2 = getRandomInt(1, 10)
        }else{
            num2 = getRandomInt(10, 100)
            num1 = getRandomInt(1, 10)
        }
    }
    else if (level % 6 === 2){
        if (choice ===  0){
            num1 = getRandomInt(100, 1000)
            num2 = getRandomInt(1, 10)
        }else{
            num2 = getRandomInt(100, 1000)
            num1 = getRandomInt(1, 10)
        }
    }
    else if (level % 6 === 3){
        num1 = getRandomInt(10, 100)
        num2 = getRandomInt(10, 100)
    }
    else if (level % 6 === 4){
        if (choice ===  0){
            num1 = getRandomInt(100, 1000)
            num2 = getRandomInt(10, 100)
        }else{
            num2 = getRandomInt(100, 1000)
            num1 = getRandomInt(10, 100)
        }
    }
    else if (level % 6 === 5){
        num1 = getRandomInt(100, 1000)
        num2 = getRandomInt(100, 1000)
    }

    let expression = num1 + " " + sign + " " + num2
    let answer = eval(expression)
    return {task: expression + " = ", answer: answer}
}

function generateQuestion(level_configuration){
    let vars = level_configuration.vars
    let expression = ''
    let answer = ''
    if (level_configuration.num_vars === 2){
        let n1 = getRandomInt(vars.n1_start, vars.n1_end)
        let n2 = getRandomInt(vars.n2_start, vars.n2_end)
        let sign = '+'
        if (vars.sign === 0){
            let choice = getRandomInt(0, 2)
            if (choice === 1){
                sign = '-'
            }
        }else{
            sign = '*'
        }
        expression = n1 + ' ' + sign + ' ' + n2
        answer = eval(expression)
    }else{
        let n1 = getRandomInt(vars.n1_start, vars.n1_end)
        let n2 = getRandomInt(vars.n2_start, vars.n2_end)
        let n3 = getRandomInt(vars.n3_start, vars.n3_end)
        let sign = getRandomInt(0, 2) === 0? '+' : '-'
        expression = '(' + n1 + ' ' + sign + ' ' + n2 + ')' + '*' + n3
        answer = eval(expression)
    }
    return {task: expression + " = ", answer: answer}
}

// eslint-disable-next-line no-unused-vars
function generateQuestion3(){


}

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //Максимум не включается, минимум включается
}



/* def create_easy_task(self, room, index):
        nums_range = 10
        n1, n2, n3 = randint(1, nums_range), randint(1, nums_range), randint(1, nums_range)
        content = "({} + {}) * {}".format(n1, n2, n3)
        answer = (n1 + n2) * n3
        task = self.create(content=content, answer=answer, room=room, index=index)
        return task*/

