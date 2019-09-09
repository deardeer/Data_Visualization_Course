##Exercise 1: 'Hello World' in HTML, Javascript

### 工具：
Sublime Text: 代码编辑器
d3.v3.min.js: https://d3js.org

###HTML
* 一个网页: index.html
* 基本结构
```
	<html>
		<head></head>
		<body></body>
	</html>
```
* 更多阅读：《html入门》：https://www.w3school.com.cn/html/html_getstarted.asp

###Javascript
* 基本语法，例如变量的声明
```
		var text = 'hello world'

		var viscourse = {
			'name': 'vis',
			'lecturer': 'min'
		}
```
* 更多阅读：《javascript教程》：https://www.runoob.com/js/js-tutorial.html
### d3.js的使用
* SVG的理解
* 画一个图元
```
	var svg = d3.select('svg')
	  .attr('width', '700px')
	  .attr('height', '700px')

	svg.append('rect')
	   .attr('x', '100px')
	   .attr('y', '100px')
	   .attr('width', '100px')
	   .attr('height', '100px')
	   .style('fill', 'green')
```
* 更多阅读：《d3.js入门教程》：http://wiki.jikexueyuan.com/project/d3wiki/
### CSS
* 更多阅读：《CSS入门教程》：https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Getting_started

