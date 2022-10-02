const profiles = JSON.parse(document.getElementById('board-data').textContent);
const colors =['white','blue','green','yellow','red']
let chartData=[]
let tableData=[]
console.log(profiles)
profiles.forEach((profile,index) => {
    if(profile.data.length !== 0){
        if(index<5){
            let XY = []
            profile.data.forEach(xy=>{
                XY.push({x:new Date(xy[0]),y:xy[1]})
            });
            let chat_data = {
                label: profile.username,
                borderColor: colors.pop(),
                steppedLine: true,
                data: XY
            };
            chartData.push(chat_data)
        }
        profile.data[0][0] = "March 12, 2022 21:00:00"
        let starttime = new Date(profile.data[0][0])
        let endtime = new Date(profile.data[profile.data.length-1][0])

        let table_data ={
            user: profile.username,
            solved: profile.correct,
            time : timeDiffCalc(endtime, starttime),
            score: profile.finalScore,
            millisec: Math.abs(endtime - starttime)
        }
        tableData.push(table_data)
    }else{
        let table_data ={
            user: profile.username,
            solved: profile.correct,
            time : 0,
            score: profile.finalScore,
            millisec: 0
        }
        tableData.push(table_data)
    }
});

var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: chartData
    },
    options: {
        scales: {
            yAxes: [{
                type: 'linear'
            }],
            xAxes: [{
                type: 'time',
                distribution: 'series', // or linear
                time: {
                    unit: 'month',
                    displayFormats: {
                        month: 'MMM D h:mm a'
                    },
                    tooltipFormat: 'MMM D h:mm a'
                }
            }]
        }
    }
});
function timeDiffCalc(dateFuture, dateNow) {
    let diffInSeconds = Math.abs(dateFuture - dateNow) / 1000;

    const days = Math.floor(diffInSeconds / 86400);
    diffInSeconds -= days * 86400;

    const hours = Math.floor(diffInSeconds / 3600) % 24;
    diffInSeconds -= hours * 3600;

    const minutes = Math.floor(diffInSeconds / 60) % 60;
    diffInSeconds -= minutes * 60;

    let difference = '';
    if (days > 0) {
        difference += (days === 1) ? `${days} day, ` : `${days} days, `;
    }
    if(hours > 0){
        difference += (hours === 0 || hours === 1) ? `${hours} hour, ` : `${hours} hours, `;
    }

    difference += (minutes === 0 || minutes === 1) ? `${minutes} minute` : `${minutes} minutes`; 

    return difference;
}

let newTableData=[]
function sortByTime(Array){
    Array.sort((a,b) => a.millisec - b.millisec)
    Array.forEach(e => {
        newTableData.push(e)
    });
}
function sortTable(){
    let key=tableData[0].score;
    let i=1;
    let start=0;
    let end=0;
    while(i<tableData.length){
        if(tableData[i].score !== key && end===start){
            end=i;
            sortByTime(tableData.slice(start,end));
            start=end;
            end=start;
            key=tableData[i].score;
        }
        i++;
    }
    sortByTime(tableData.slice(start,i));
}
sortTable();

let table = document.getElementById('table')
let table_html=''
newTableData.forEach((profile,idx) => {
    table_html+=`
    <tr>
        <th scope="row">${idx+1}</th>
            <td>${profile.user}</td>
            <td>${profile.solved}</td>
            <td>${profile.time}</td>
            <td>${profile.score}</td>
    </tr>
    `
});
table.innerHTML = table_html