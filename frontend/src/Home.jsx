import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import PicksSummary from './PicksSummary.jsx';

function HomePage() {
    return (
        <>
            {/* Navbar */}
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <div className="container-fluid">
                    <a className="navbar-brand" href="#">$$$</a>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <a className="nav-link active" aria-current="page" href="#">Home</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Features</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Pricing</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            {/* Hero Section */}
            <div className="p-5 mb-4 bg-light rounded-3">
                <div className="container-fluid py-5">
                    <div className="summary-picks">
                        <PicksSummary />
                    </div>
                    <p className="col-md-8 fs-4"></p>
                </div>
            </div>

            {/* Footer */}
            <footer className="bg-dark text-center text-white">
                <div className="container p-4">
                    <section className="mb-4">
                        <p>The footer</p>
                    </section>
                </div>
            </footer>
        </>
    );
}

export default HomePage;
