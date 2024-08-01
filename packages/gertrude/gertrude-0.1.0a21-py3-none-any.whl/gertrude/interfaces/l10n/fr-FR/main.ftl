# Gertrude --- GTD done right
# Copyright © 2023, 2024 Tanguy Le Carrour <tanguy@bioneland.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

-project-name = Gertrude

activities-capture = Capturer
activities-clarify = Clarifier
activities-organize = Organiser
activities-reflect = Refléchir
activities-engage = Agir

categories-inbox = Boite de réception
categories-organize = Organiser
categories-next = Suivantes
categories-projects = Projets
categories-waiting = Déléguées
categories-scheduled = Programmées
categories-someday = Plus tard

exceptions-unknown-exception = Une erreur inconnue est survenue ! [`{ $name }`]
exceptions-missing-value = Cette valeur est obligatoire !
exceptions-transition-not-allowed = Cette transition est impossible !
exceptions-date-in-the-past = La date ne peut pas être dans le passé !
exceptions-string-too-long =
    { $max ->
        [one] Cette valeur doit faire au maximum un caractère !
       *[other] Cette valeur doit faire au maximum { $max } caractères !
    }
exceptions-string-too-short =
    { $min ->
        [one] Cette valeur doit faire au minimum un caractère !
       *[other] Cette valeur doit faire au minimum { $max } caractères !
    }
exceptions-not-found = La page que vous cherchez n’existe pas !

pages-layout-title = { -project-name }
pages-layout-footer-html =
    <p>
        Version { $version } © { $years } Bioneland.
        <br />
        Le code est sous licence <a href="https://www.gnu.org/licenses/agpl-3.0.fr.html">AGPL</a>.
    </p>

pages-navbar-login = Se connecter
pages-navbar-logout = Se déconnecter

pages-mixins-actions-do = Marquer comme fait !
pages-mixins-actions-delegate = Déléguer !
pages-mixins-actions-postpone = Marquer comme actionnable !
pages-mixins-actions-file = Classer !
pages-mixins-actions-incubate = Garder pour plus tard.
pages-mixins-actions-eliminate = Éliminer !
pages-mixins-actions-reclaim = Reprendre à { $current_person } !
pages-mixins-actions-assign = Assigner !
pages-mixins-actions-reassign = Assignée à { $current_project }.
pages-mixins-actions-schedule = Programmer !
pages-mixins-actions-reschedule = Programmée pour le { $current_date }.
pages-mixins-actions-projectify = En faire un projet !
pages-mixins-list-of-tasks-display-title = Afficher la tâche
pages-mixins-list-of-tasks-display-label = Voir
pages-mixins-list-of-tasks-update-title = Éditer la tâche
pages-mixins-list-of-tasks-update-label = Éditer

pages-modal-close = fermer

pages-auth-login-title = Se connecter à { -project-name }
pages-auth-login-link = S'identifier avec { $label }
pages-auth-ip-error = Erreur lors de l’authentification par IP.
pages-auth-totp-error = Erreur lors de l’authentification par TOTP.

pages-totp-login-title = Connexion
pages-totp-login-description = Merci de saisir votre mot de passe à usage unique.
pages-totp-login-password = Mot de passe
pages-totp-login-pattern = Un code TOTP se compose de 6 chiffres.
pages-totp-login-action = Se connecter

pages-error-title = Une erreur est survenu !
pages-error-unauthorized = Vous n’êtes pas autorisé·e à voir cette page !
pages-error-csrf-expired =
    Le jeton de sécurité CSRF n’est pas correct ! Cela ne devrait pas arriver, désolé !

pages-root-title = Bienvenue sur { -project-name } !
pages-root-subtitle = Un système de gestion de tâches.
pages-root-introduction-html =
    The heartbeat of GTD is <strong>five simple steps</strong> that apply order to chaos
    and provide you the space and structure to be more creative, strategic
    and focused.
pages-tasks-root-capture-title = Capture — collect what has your attention
pages-tasks-root-capture-description-html =
    Use an in-tray, notepad, digital list or voice recorder to capture
    everything that has your attention.
    <br />
    Little, big, personal and professional — all your to-do's, projects,
    things to handle or finish.
pages-tasks-root-clarify-title = Clarify — process what it means
pages-tasks-root-clarify-description-html =
    Take everything that you capture and ask; is it actionable?
    <br />
    If no, then trash it, incubate it, or file it as reference.
    <br />
    If yes, decide the very next action required. If it will take less
    than two minutes, do it now. If not, delegate it if you can; or put
    it on a list to do when you can.
pages-tasks-root-organize-title = Organize — put it where it belongs
pages-tasks-root-organize-description-html =
    Put action reminders on the right lists. For example, create lists for
    the apropriate categories — calls to make, errands to run, emails to send, etc.
pages-tasks-root-reflect-title = Reflect — review frequently
pages-tasks-root-reflect-description-html =
    Look over your lists as often as necessary to trust your choices about
    what to do next. Do a weekly review to get clear, get current and creative.
pages-tasks-root-engage-title = Engage — simply do
pages-tasks-root-engage-description-html =
    Use your system to take appropriate actions with confidence.

pages-projects-display-actionable-tasks-title = Tâches actionnables
pages-projects-display-actionable-tasks-empty =
    Il n'y a aucune tâche actionnable pour ce projet.
    Merci d'en sélectionner une dans la liste des tâches incubées.
pages-projects-display-incubated-tasks-title = Tâches incubées
pages-projects-display-incubated-tasks-empty =
    Il n'y a aucune tâche incubée pour ce projet.
    Vous pouvez en capturer de nouvelles.
pages-projects-display-nothing-to-do-html =
    <p>Félicitations ! Il n'y plus de tâches à faire pour ce projet.</p>
    <p>
        Si le projet n'est pas encore fini, vous pouvez capturer de nouvelles tâches
        ou vous pouvez le considéré comme terminé et l'archiver.
    </p>
pages-projects-display-done-tasks-title = Tâches déjà réalisées
pages-projects-display-done-tasks-empty = Aucune tâche n'a pour le moment été réalisée pour ce projet.
pages-projects-display-project-not-found = Le projet auquel vous essayez d'accéder n'existe pas !

pages-projects-create-title = Créer un nouveau projet
pages-projects-create-short-name-label = Nom court
pages-projects-create-short-name-help = Utilisé pour les badges partout où le nom est trop long pour être affiché (max. { $max }).
pages-projects-create-name-label = Nom
pages-projects-create-name-help = Le nom du projet (max. { $max }).
pages-projects-create-submit = Créer
pages-projects-create-cancel = Annuler
pages-projects-create-missing-id = Vous devez fournir un ID !
pages-projects-create-missing-name = Vous devez fournir un nom !
pages-projects-create-missing-short-name = Vous devez fournir un nom court !
pages-projects-create-project-already-exists = Le projet existe déjà !
pages-projects-create-project-name-already-used = Ce nom est déjà utilisé !
pages-projects-create-project-short-name-already-used = Ce nom court est déjà utilisé !

pages-projects-list-title = Vos projets
pages-projects-list-empty = Il n'y a aucun projet à afficher.
pages-projects-list-new = Nouveau projet
pages-projects-list-view = Voir

pages-tasks-errors-task-not-found = Impossible de trouver la tâche !
pages-tasks-errors-transition-not-allowed = Cette transition n'est pas possible !

pages-tasks-list-title = Organisez vos tâches
pages-tasks-list-empty-html = <p>Il n'y a aucune tâche à afficher. Capturez en de nouvelles.</p>
pages-tasks-list-captured-title = Boîte de réception
pages-tasks-list-captured-empty-html =
    <p>
        Votre boite de réception est vide !
        <br />
        Trouver la prochaine sur
        <a href="{ $url_next }">
            <span>la page des tâches à réaliser</span>
                <span class="icon-text">
                    <span class="icon">
                        <span class="fas fa-chevron-circle-right"></span>
                    </span>
                </span>
            </span>
        </a>
    </p>
pages-tasks-list-actionable-title = Prochaines tâches
pages-tasks-list-actionable-empty-html =
    <p>
        Félicitations ! Votre liste des choses à faire est vide !
        <br />
        Réfléchisser à et passer en revue vos listes de tâches
        <a href="{ $url_delegated }">
            <span>déléguées</span>
            <span class="icon-text"><span class="icon"><span class="fas fa-coffee"></span></span></span>
        </a>,
        <a href="{ $url_scheduled }">
            <span>programmées</span>
            <span class="icon-text"><span class="icon"><span class="fas fa-calendar"></span></span></span>
        </a> et
        <a href="{ $url_incubated }">
            <span>repoussées</span>
            <span class="icon-text"><span class="icon"><span class="fas fa-umbrella"></span></span></span>
        </a>
        pour trouver quoi faire ensuite.
    </p>
pages-tasks-list-scheduled-title = Tâches programmées
pages-tasks-list-scheduled-empty-html = <p>Vous n'avez aucune tâches programmées.</p>
pages-tasks-list-incubated-title = Tâches incubées
pages-tasks-list-incubated-empty-html = 
    <p>
        Vous n'avez aucune tâches incubées pour plus tard. Capturez en de nouvelles !
    </p>
    <p>
        Remarquez que seules les tâches non-assignées sont listées ici.
        Pensez à consulter <a href="{ $url_projects }">votre liste de projets</a>.
    </p>
pages-tasks-list-delegated-title = Tâches déléguées
pages-tasks-list-delegated-empty = <p>Vous n'avez aucune tâches déléguées à d'autres personnes.</p>

pages-tasks-display-title = Détails de la tâche
pages-tasks-display-update-label = Éditer
pages-tasks-display-update-title = Éditer les détails de la tâche
pages-tasks-display-assigned-to = Assignée à
pages-tasks-display-delegated-to = Déléguée à
pages-tasks-display-what-next = Décider ce qu'il faut faire ensuite
pages-tasks-display-is-actionable = Est-elle actionnable ?
pages-tasks-display-yes = Oui
pages-tasks-display-no = Non
pages-tasks-display-conditions-do = Si cela prend moins de 2 minutes…
pages-tasks-display-conditions-delegate = Si quelqu'un d'autre peut le faire pour vous…
pages-tasks-display-conditions-projectify = Si cela nécessite plusieurs étapes…
pages-tasks-display-conditions-postpone = Sinon…
pages-tasks-display-conditions-assign = Si cela fait partie d'un projet…
pages-tasks-display-conditions-schedule = Si cela doit être réalisé à un autre moment…
pages-tasks-display-conditions-incubate = Si vous voulez le faire dans le futur…
pages-tasks-display-conditions-file = Si vous voulez juste le garder pour référence…
pages-tasks-display-conditions-eliminate = Sinon…
pages-tasks-display-no-action = Il n'y a rien à faire de plus pour cette tâche !

pages-tasks-capture-page-title = Capturer une tâche
pages-tasks-capture-title-placeholder = Un titre
pages-tasks-capture-description-placeholder = Une description optionnelle
pages-tasks-capture-submit = Capturer
pages-tasks-capture-cancel = Annuler
pages-tasks-capture-task-id-already-used = Cette ID de tâche est déjà utilisé !?
pages-tasks-capture-taks-captured = Tâche capturée !

pages-tasks-update-page-title = Mettre à jour une tâche
pages-tasks-update-title-placeholder = Un titre
pages-tasks-update-description-placeholder = Une description optionnelle
pages-tasks-update-submit = Mettre à jour
pages-tasks-update-cancel = Annuler
pages-tasks-update-success = Tâche mise à jour !

pages-tasks-assign-title = Assigner une tâche à un projet.
pages-tasks-assign-project-id-label = Projet
pages-tasks-assign-project-id-help = Nom du projet auquel assigner la tâche.
pages-tasks-assign-submit = Assigner
pages-tasks-assign-cancel = Annuler
pages-tasks-assign-missing-project-id = ID de projet manquant !
pages-tasks-assign-incorrect-project-id = ID de projet incorrect !
pages-tasks-assign-project-not-found = Impossible de trouver le projet !
pages-tasks-assign-success = Tâche assignée !

pages-tasks-delegate-title = Déléguer une tâche à une personne
pages-tasks-delegate-person-label = Personne à qui déléguer
pages-tasks-delegate-person-placeholder = Nom de la personne à qui déléguer la tâche
pages-tasks-delegate-submit = Déléguer
pages-tasks-delegate-cancel = Annuler
pages-tasks-delegate-success = Tâche déléguée !

pages-tasks-do-success = Tâche marquée comme réalisée !

pages-tasks-eliminate-success = Tâche éliminée !

pages-tasks-file-success = Tâche classée !

pages-tasks-incubate-success = Tâche incubée !

pages-tasks-postpone-success = Tâche marquée comme actionnable.

pages-tasks-reclaim-success = Tâche récupérée !

pages-tasks-schedule-title = Programmer une tâche pour une date
pages-tasks-schedule-date-help = Date à laquelle la tâche doit être réalisée.
pages-tasks-schedule-next-week = dans 1 semaine
pages-tasks-schedule-next-month = dans 1 moins
pages-tasks-schedule-submit = Programmer
pages-tasks-schedule-cancel = Annuler
pages-tasks-schedule-success = Tâche programmée !
