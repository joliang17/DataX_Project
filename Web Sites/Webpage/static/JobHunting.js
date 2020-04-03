// define initial variables

var name, worked_before, work_year, major, skill_other;

var checked_skill = [];
var unchecked_skill = [];

// onclick event on 'check to see the result' button
$(document).ready(function(){
    $('#CheckResult').click(function(){
        // name
        name = document.getElementById("name").value;

        // if worked before & work experience
        worked_before = $('input[name=yesorno]:checked').val();
        work_year = document.getElementById("work_experience_year").value;

        // major
        major = $('#MajorSelection').find(":selected").text();

        // skills
        checked_skill = []
        $.each($("input[name='SkillCheckBox']:checked"), function(){
            checked_skill.push($(this).val());
        });
        unchecked_skill = []
        $.each($("input[name='SkillCheckBox']:not(:checked)"), function(){
            unchecked_skill.push($(this).val());
        });
        var temp = document.getElementById("skill_other").value;
        skill_other = temp.split(",");

        // call api functions
        GetResults()
    });
});

function GetResults(){
    $.ajax({
        type:"get",
        url: "http://localhost:5000/results", 
        success: function(result){
            temp = result.replace(/\[/g,'').replace(/\]/g,'').split(",");
            
            var data = [];
            while(temp.length) 
            data.push(temp.splice(0,3));

            AddResulttoTable(data)
      }});
};

function AddResulttoTable(data){
    var tableData = ""
    for(var i=0; i<data.length; i++){
        
        tableData += "<tr>"
        for(var j=0; j<data[i].length; j++){
            tableData+="<td>"+data[i][j]+"</td>"
        }
        tableData += "</tr>"
    }
    $("#Recommendation").append(tableData)
  };