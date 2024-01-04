import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
    faEnvelope,
    faEyeSlash,
    faArrowRight,
} from "@fortawesome/free-solid-svg-icons";
import Link from "next/link";
import "./form-auth.css";

export default function FormAuth({ isLogin, isSignIn }) {
    return (
        <form method="POST" className="login-form">
            <div className="form">
                <div className="form-row">
                    <FontAwesomeIcon icon={faEnvelope} className="form-icon" />
                    <label className="form-label">Email</label>
                    <input type="text" className="form-text" name="email" />
                </div>
                <div className="form-row">
                    <FontAwesomeIcon icon={faEyeSlash} className="form-icon" />
                    <label className="form-label">Password</label>
                    <input
                        type="password"
                        className="form-text"
                        name="Password"
                    />
                </div>
                {isLogin ? (
                    <>
                        <div className="form-row">
                            <div className="form-check">
                                <input type="checkbox" id="remember" />
                                <label htmlFor="remember">remember me?</label>
                            </div>
                        </div>
                        <div className="another">
                            <span>
                                Don't have an account yet?{" "}
                                <Link href="/register">Sign up</Link>
                            </span>
                        </div>
                    </>
                ) : (
                    ""
                )}
                {isSignIn ? (
                    <div className="another">
                        <span>
                            Already have an account?{" "}
                            <Link href="/login">Log in</Link>
                        </span>
                    </div>
                ) : (
                    ""
                )}
                <div className="form-row">
                    <button className="btn btn-login">
                        {" "}
                        {isLogin ? "Login" : "Create"}
                        <FontAwesomeIcon icon={faArrowRight} />
                    </button>
                </div>
            </div>
        </form>
    );
}
