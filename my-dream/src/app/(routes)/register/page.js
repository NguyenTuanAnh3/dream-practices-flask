import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUserCircle } from "@fortawesome/free-solid-svg-icons";
import FormAuth from "@/app/components/form/FormAuth";

export default function page() {
    return (
        <div className="auth text-center">
            <FontAwesomeIcon icon={faUserCircle} width="30px" color="#4d61fc" />
            <strong>Create account!</strong>
            <FormAuth isSignIn={true} />
        </div>
    );
}
