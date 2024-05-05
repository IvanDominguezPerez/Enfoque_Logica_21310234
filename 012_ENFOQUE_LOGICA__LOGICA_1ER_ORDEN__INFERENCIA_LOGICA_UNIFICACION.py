class Unifier:
    @staticmethod
    def unify(term1, term2, substitution=None):
        """Realiza la unificación de dos términos lógicos.

        Args:
            term1: El primer término lógico.
            term2: El segundo término lógico.
            substitution: La sustitución actual.

        Returns:
            La sustitución que hace que los términos sean idénticos, o None si no es posible unificar.
        """
        if substitution is None:
            substitution = {}

        if term1 == term2:
            return substitution

        if isinstance(term1, str) and term1[0].islower():
            return Unifier._unify_variable(term1, term2, substitution)

        if isinstance(term2, str) and term2[0].islower():
            return Unifier._unify_variable(term2, term1, substitution)

        if isinstance(term1, list) and isinstance(term2, list):
            if len(term1) != len(term2):
                return None
            for t1, t2 in zip(term1, term2):
                substitution = Unifier.unify(t1, t2, substitution)
                if substitution is None:
                    return None
            return substitution

        return None

    @staticmethod
    def _unify_variable(variable, value, substitution):
        """Realiza la unificación de una variable con un valor.

        Args:
            variable: La variable.
            value: El valor.
            substitution: La sustitución actual.

        Returns:
            La sustitución que hace que la variable sea igual al valor.
        """
        if variable in substitution:
            return Unifier.unify(substitution[variable], value, substitution)
        elif value in substitution:
            return Unifier.unify(variable, substitution[value], substitution)
        else:
            substitution[variable] = value
            return substitution

# Ejemplo de uso
term1 = ['f', 'X', 'Y']
term2 = ['f', 'a', 'b']

substitution = Unifier.unify(term1, term2)

if substitution is not None:
    print("Unificación exitosa. Sustitución:")
    for var, val in substitution.items():
        print(var, "=", val)
else:
    print("No se puede unificar los términos.")
