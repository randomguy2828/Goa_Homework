const container = document.getElementById('container');

const paragraph = document.createElement('p');
const paragraphText = document.createTextNode('Hellow World');
paragraph.appendChild(paragraphText);
container.appendChild(paragraph);

const button = document.createElement('button');
const buttonText = document.createTextNode('click me');
button.appendChild(buttonText);
container.appendChild(button);

const image = document.createElement('img');
image.src = 'https://bocdn.ecotree.green/blog/0001/01/ad46dbb447cd0e9a6aeecd64cc2bd332b0cbcb79.jpeg?d=960x540'; 
image.alt = 'tree';
container.appendChild(image);

button.remove();

const newParagraph = document.createElement('p');
const newParagraphText = document.createTextNode('Only text');
newParagraph.appendChild(newParagraphText);
container.replaceChild(newParagraph, image);