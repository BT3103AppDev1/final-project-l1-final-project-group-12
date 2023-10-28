<template>
    <div id="bigLogo">
      <img src="../assets/logo/logo.png">
    </div>

    <div id="information1">
      <h2 id="info1">Diversify your portfolio and minimise risk. <br> Learn how to maximise your returns today!</h2>
      <img src="../assets/logo/PLACEHOLDERSCREENSHOT.png"><br>      
      <button id="signUpButton">Sign up now!</button>
    </div>

    <div id="information2">
        <div id="info2Container2">
            <h2 id="info3">Keep track of all your investments in one place</h2>
        </div>
        <div id="info2Container1">
            <div id="portfolioSection">
                <h2 id="info2">Portfolio Overview</h2>
                <img src="../assets/logo/pieChart.png" alt="Pie Chart">
            </div>
        </div>
    </div>

    <div id="information3">
        <img src="../assets/logo/riskMeter.png" alt="riskMeter">

      <div id="info4Container">
        <h2 id="info4">Portfolio risks are calculated automatically</h2>
      </div>
      
    </div>
</template>

<style scoped>
#bigLogo {
    background-color: #0E295B;
    height: 45vw;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center; 
}

#bigLogo img {
    height: 12.9vw;
    width: 55vw;
}

#information1 {
    height: 50vw;
    text-align: center;
}

#info1 {
    padding-top: 3vw;
    font-size: 2.1vw;
    font-weight: 700;
    font-family: 'Inter', sans-serif;
    color: #000;
    text-align: center;
    font-style: normal;
    line-height: normal;
    letter-spacing: -0.02vw;
}

#information1 img {
    height: 30vw;
    width: 57.6vw;
    padding-bottom: 2vw;
}

#signUpButton {
    width: 11.8vw;
    height: 2.6vw;
    color: #000;
    text-align: center;
    font-family: 'Inter', sans-serif;
    font-size: 1vw;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    letter-spacing: -0.016vw;
    border-radius: 1vw;
    border: 0.06vw solid #000;
    background: #D8D6F5;
    box-shadow: 0px 0.24vw 0.24vw 0px rgba(0, 0, 0, 0.25);
}

#information2 {
    height: 38vw;
    background: #272F51;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 4vw; 
}

#info2Container1 {
    text-align: center;  
    flex: 3;
    display: flex;
    justify-content: center;
    align-items: center;
}

#info2Container1 img {
    height: 25vw;
    width: 27.6vw;
    margin-top: 2vw;
}

#info2Container2 {
    text-align: center;  
    flex: 5;
    max-width: 50%;  /* Limit the width to 50% of the container */
    box-sizing: border-box;  /* This ensures padding is included in the width */
}

#info2, #info3 {
    color: #FFF;
    font-family: 'Inter', sans-serif;
    font-size: 3vw;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    letter-spacing: -0.02vw;
    margin-bottom: 1vw; 
    margin-right: 4vw; /* Add some right margin to prevent overflow */
}

#info2 {
    margin-bottom: 4vw;
}

#portfolioSection {
    display: inline-block;
}



#information3 {
    height: 38vw;
    background: #ffffff;
    display: flex;
    justify-content: center;
    align-items: center; 
}

#information3 img {
    width: 47vw;
    height: 25vw;
    padding-left: 4.8vw;
}

#info4Container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
}

#info4 {
    color: #000;
    text-align: center;
    font-family: 'Inter', sans-serif;
    font-size: 2.1vw;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
    letter-spacing: -0.02vw;
    max-width: 42vw;
    padding: 1.2vw;
}

#information2 h2, #information3 h2 {
    margin: 0;
}

#signUpButton:hover {
    text-decoration: underline;
    cursor: pointer;
}


</style>


