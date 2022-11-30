function generatePDF() {
    // Choose the element that our invoice is rendered in.
    const element = document.getElementById('resumeTempl');


    var opt = {
            // margin:       [0.1, 0.1,0.1,0.1],
            filename:     'myfile.pdf',
            // image:        { type: 'jpeg', quality: 0.99 },
            html2canvas:  { scale:5 },
            // jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' },
            // jsPDF:        { unit: 'in', format: 'letter', orientation: 'l' },

            jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' },
// 
            pagebreak:     {mode: ['avoid-all','css','legacy']},

            // pagebreak:     {mode: ['avoid-all','css']},
            // pagebreak:     {mode: ['avoid-all']},

            // pagebreak:     {mode: ['css']},
            // pagebreak:     {mode: ['legacy']}


            };

                    // Choose the element and save the PDF for our user.
    // New Promise-based usage:
    html2pdf().set(opt).from(element).save();
}

