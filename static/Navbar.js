import React from 'react'
import { Link } from "react-router-dom";

const NavBar = () => {

    return (
        <div>
            <nav className="navbar fixed-top navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/http://127.0.0.1:5000/project.html">CareCast</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">

                            <li className="nav-item"><Link className="nav-link" to="/diabetes">Diabetes</Link></li>
                            <li className="nav-item"><Link className="nav-link" to="/kidney-disease">Kidney-disease</Link></li>
                            <li className="nav-item"><Link className="nav-link" to="/heart-disease">Heart-disease</Link></li>
                            <li className="nav-item"><Link className="nav-link" to="/breast-cancer">Breast-cancer</Link></li>
                            <li className="nav-item"><Link className="nav-link" to="/ayurveda">ayurveda</Link></li>

                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    )

}

export default NavBar