import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSignInAlt } from "@fortawesome/free-solid-svg-icons";
import FormAuth from "@/app/components/form/FormAuth";

export default function page() {
    return (
        <div className="auth text-center">
            <FontAwesomeIcon icon={faSignInAlt} width="30px" color="#4d61fc"/>
            <strong>Welcome!</strong>
            <span>Login to your account</span>
            <FormAuth isLogin={true} />
        </div>
    )
}