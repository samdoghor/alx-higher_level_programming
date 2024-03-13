#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP 
{
	charPrint (c) 
	{
		let i=0;

                while (i < this.height)
                {
			if (c === undefined)
			{
				let line = 'X';
				console.log(line.repeat(this.width))
			} else
			{
				let line = 'C';
				console.log(line.repeat(this.width))
			}
                        i += 1;
                }
	}
}

module.exports = Square
