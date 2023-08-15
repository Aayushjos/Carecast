// import './App.css';
import React, { useState } from 'react'


import NavBar from './Navbar';
import Blogs from './Blogs';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import LoadingBar from 'react-top-loading-bar'

const App = () => {
    const pageSize = 5;
    const apiKey = "08f901411d7f40f48d344133f31109a4";
    const [progress, setProgress] = useState(0)

    return (
        <div>
            <Router>
                <NavBar/>
                <LoadingBar
                    height={3}
                    color='#f11946'
                    progress={progress}
                />
                <Switch>
                    <Route exact path="/Diabetes"><Blogs setProgress={setProgress} apiKey={apiKey} key="Diabetes" pageSize={pageSize} q={Diabetes} /></Route>
                    <Route exact path="/Kidney-disease"><Blogs setProgress={setProgress} apiKey={apiKey} key="Kidney-disease" pageSize={pageSize} q={Kidney - disease} /></Route>
                    <Route exact path="/Heart-disease"><Blogs setProgress={setProgress} apiKey={apiKey} key="Heart-disease" pageSize={pageSize} q={Heart - disease} /></Route>
                    <Route exact path="/Breast-cancer"><Blogs setProgress={setProgress} apiKey={apiKey} key="Breast-cancer" pageSize={pageSize} q={Breast - cancer} /></Route>
                    <Route exact path="/ayurveda"><Blogs setProgress={setProgress} apiKey={apiKey} key="ayurveda" pageSize={pageSize} q={ayurveda} /></Route>
                </Switch>
            </Router>
        </div>
    )

}

export default App;