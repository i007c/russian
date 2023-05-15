// const http = require('http')
const jsdom = require('jsdom')
const fs = require('fs')

async function main() {
    let words = []

    for (let i = 1; i <= 12; i++) {
        let url = `http://masterrussian.com/vocabulary/most_common_words_${i}.htm`
        if (i == 1) {
            url = 'http://masterrussian.com/vocabulary/most_common_words.htm'
        }

        let result = await jsdom.JSDOM.fromURL(url)

        result.window.document
            .querySelector('table.topwords')
            .querySelectorAll('tr')
            .forEach(row => {
                if (row.className == 'rowTop') return

                let items = Array.from(row.children).filter(
                    el => el.textContent
                )

                if (items.length != 4) {
                    throw Error('bad item', items[0].textContent)
                }

                let rank = +items[0].textContent
                let russian = items[1].textContent.trim()
                let english = items[2].textContent.trim()
                let type = items[3].textContent.trim()

                // console.log(i, rank, russian, english, type)

                words.push({ rank, russian, english, type })
            })
        console.log(i, 'done')
    }

    console.log('total:', words.length)

    fs.writeFileSync('words.json', JSON.stringify(words), {
        // mode: 'w',
        encoding: 'utf8',
    })
}

main()

// http.get(url, res => {
//     let data = []
//     res.on('data', chunk => {
//         data.push(chunk)
//     })
//
//     res.on('end', () => {
//         let result = Buffer.concat(data).toString()
//         let document = parser.parseFromString(result, 'text/html')
//         console.log(document)
//     })
// })
