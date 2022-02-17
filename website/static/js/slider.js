let imagesCount = 4;

let counter = 1;

document.getElementById('radio' + counter).checked = true;

let timer = setInterval(slide, 5000);

for (let i=1; i<=imagesCount; i++) {
    document.getElementById('radio' + i)
            .addEventListener('change', () => {
                counter = i;
                clearInterval(timer);
                timer = setInterval(slide, 5000);
            })
}


function slide() {
    counter++;
    if (counter > imagesCount) {
        counter = 1;
    }

    document.getElementById('radio' + counter).checked = true;
}