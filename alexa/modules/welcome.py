from alexa import spamcheck
#                         GNU AFFERO GENERAL PUBLIC LICENSE
#                            Version 3, 19 November 2007
#
#      Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
#      Everyone is permitted to copy and distribute verbatim copies
#      of this license document, but changing it is not allowed.
#
#                                 Preamble
#
#       The GNU Affero General Public License is a free, copyleft license for
#     software and other kinds of works, specifically designed to ensure
#     cooperation with the community in the case of network server software.
#
#       The licenses for most software and other practical works are designed
#     to take away your freedom to share and change the works.  By contrast,
#     our General Public Licenses are intended to guarantee your freedom to
#     share and change all versions of a program--to make sure it remains free
#     software for all its users.
#
#       When we speak of free software, we are referring to freedom, not
#     price.  Our General Public Licenses are designed to make sure that you
#     have the freedom to distribute copies of free software (and charge for
#     them if you wish), that you receive source code or can get it if you
#     want it, that you can change the software or use pieces of it in new
#     free programs, and that you know you can do these things.
#
#       Developers that use our General Public Licenses protect your rights
#     with two steps: (1) assert copyright on the software, and (2) offer
#     you this License which gives you legal permission to copy, distribute
#     and/or modify the software.
#
#       A secondary benefit of defending all users' freedom is that
#     improvements made in alternate versions of the program, if they
#     receive widespread use, become available for other developers to
#     incorporate.  Many developers of free software are heartened and
#     encouraged by the resulting cooperation.  However, in the case of
#     software used on network servers, this result may fail to come about.
#     The GNU General Public License permits making a modified version and
#     letting the public access it on a server without ever releasing its
#     source code to the public.
#
#       The GNU Affero General Public License is designed specifically to
#     ensure that, in such cases, the modified source code becomes available
#     to the community.  It requires the operator of a network server to
#     provide the source code of the modified version running there to the
#     users of that server.  Therefore, public use of a modified version, on
#     a publicly accessible server, gives the public access to the source
#     code of the modified version.
#
#       An older license, called the Affero General Public License and
#     published by Affero, was designed to accomplish similar goals.  This is
#     a different license, not a version of the Affero GPL, but Affero has
#     released a new version of the Affero GPL which permits relicensing under
#     this license.
#
#       The precise terms and conditions for copying, distribution and
#     modification follow.
#
#                            TERMS AND CONDITIONS
#
#       0. Definitions.
#
#       "This License" refers to version 3 of the GNU Affero General Public License.
#
#       "Copyright" also means copyright-like laws that apply to other kinds of
#     works, such as semiconductor masks.
#
#       "The Program" refers to any copyrightable work licensed under this
#     License.  Each licensee is addressed as "you".  "Licensees" and
#     "recipients" may be individuals or organizations.
#
#       To "modify" a work means to copy from or adapt all or part of the work
#     in a fashion requiring copyright permission, other than the making of an
#     exact copy.  The resulting work is called a "modified version" of the
#     earlier work or a work "based on" the earlier work.
#
#       A "covered work" means either the unmodified Program or a work based
#     on the Program.
#
#       To "propagate" a work means to do anything with it that, without
#     permission, would make you directly or secondarily liable for
#     infringement under applicable copyright law, except executing it on a
#     computer or modifying a private copy.  Propagation includes copying,
#     distribution (with or without modification), making available to the
#     public, and in some countries other activities as well.
#
#       To "convey" a work means any kind of propagation that enables other
#     parties to make or receive copies.  Mere interaction with a user through
#     a computer network, with no transfer of a copy, is not conveying.
#
#       An interactive user interface displays "Appropriate Legal Notices"
#     to the extent that it includes a convenient and prominently visible
#     feature that (1) displays an appropriate copyright notice, and (2)
#     tells the user that there is no warranty for the work (except to the
#     extent that warranties are provided), that licensees may convey the
#     work under this License, and how to view a copy of this License.  If
#     the interface presents a list of user commands or options, such as a
#     menu, a prominent item in the list meets this criterion.
#
#       1. Source Code.
#
#       The "source code" for a work means the preferred form of the work
#     for making modifications to it.  "Object code" means any non-source
#     form of a work.
#
#       A "Standard Interface" means an interface that either is an official
#     standard defined by a recognized standards body, or, in the case of
#     interfaces specified for a particular programming language, one that
#     is widely used among developers working in that language.
#
#       The "System Libraries" of an executable work include anything, other
#     than the work as a whole, that (a) is included in the normal form of
#     packaging a Major Component, but which is not part of that Major
#     Component, and (b) serves only to enable use of the work with that
#     Major Component, or to implement a Standard Interface for which an
#     implementation is available to the public in source code form.  A
#     "Major Component", in this context, means a major essential component
#     (kernel, window system, and so on) of the specific operating system
#     (if any) on which the executable work runs, or a compiler used to
#     produce the work, or an object code interpreter used to run it.
#
#       The "Corresponding Source" for a work in object code form means all
#     the source code needed to generate, install, and (for an executable
#     work) run the object code and to modify the work, including scripts to
#     control those activities.  However, it does not include the work's
#     System Libraries, or general-purpose tools or generally available free
#     programs which are used unmodified in performing those activities but
#     which are not part of the work.  For example, Corresponding Source
#     includes interface definition files associated with source files for
#     the work, and the source code for shared libraries and dynamically
#     linked subprograms that the work is specifically designed to require,
#     such as by intimate data communication or control flow between those
#     subprograms and other parts of the work.
#
#       The Corresponding Source need not include anything that users
#     can regenerate automatically from other parts of the Corresponding
#     Source.
#
#       The Corresponding Source for a work in source code form is that
#     same work.
#
#       2. Basic Permissions.
#
#       All rights granted under this License are granted for the term of
#     copyright on the Program, and are irrevocable provided the stated
#     conditions are met.  This License explicitly affirms your unlimited
#     permission to run the unmodified Program.  The output from running a
#     covered work is covered by this License only if the output, given its
#     content, constitutes a covered work.  This License acknowledges your
#     rights of fair use or other equivalent, as provided by copyright law.
#
#       You may make, run and propagate covered works that you do not
#     convey, without conditions so long as your license otherwise remains
#     in force.  You may convey covered works to others for the sole purpose
#     of having them make modifications exclusively for you, or provide you
#     with facilities for running those works, provided that you comply with
#     the terms of this License in conveying all material for which you do
#     not control copyright.  Those thus making or running the covered works
#     for you must do so exclusively on your behalf, under your direction
#     and control, on terms that prohibit them from making any copies of
#     your copyrighted material outside their relationship with you.
#
#       Conveying under any other circumstances is permitted solely under
#     the conditions stated below.  Sublicensing is not allowed; section 10
#     makes it unnecessary.
#
#       3. Protecting Users' Legal Rights From Anti-Circumvention Law.
#
#       No covered work shall be deemed part of an effective technological
#     measure under any applicable law fulfilling obligations under article
#     11 of the WIPO copyright treaty adopted on 20 December 1996, or
#     similar laws prohibiting or restricting circumvention of such
#     measures.
#
#       When you convey a covered work, you waive any legal power to forbid
#     circumvention of technological measures to the extent such circumvention
#     is effected by exercising rights under this License with respect to
#     the covered work, and you disclaim any intention to limit operation or
#     modification of the work as a means of enforcing, against the work's
#     users, your or third parties' legal rights to forbid circumvention of
#     technological measures.
#
#       4. Conveying Verbatim Copies.
#
#       You may convey verbatim copies of the Program's source code as you
#     receive it, in any medium, provided that you conspicuously and
#     appropriately publish on each copy an appropriate copyright notice;
#     keep intact all notices stating that this License and any
#     non-permissive terms added in accord with section 7 apply to the code;
#     keep intact all notices of the absence of any warranty; and give all
#     recipients a copy of this License along with the Program.
#
#       You may charge any price or no price for each copy that you convey,
#     and you may offer support or warranty protection for a fee.
#
#       5. Conveying Modified Source Versions.
#
#       You may convey a work based on the Program, or the modifications to
#     produce it from the Program, in the form of source code under the
#     terms of section 4, provided that you also meet all of these conditions:
#
#         a) The work must carry prominent notices stating that you modified
#         it, and giving a relevant date.
#
#         b) The work must carry prominent notices stating that it is
#         released under this License and any conditions added under section
#         7.  This requirement modifies the requirement in section 4 to
#         "keep intact all notices".
#
#         c) You must license the entire work, as a whole, under this
#         License to anyone who comes into possession of a copy.  This
#         License will therefore apply, along with any applicable section 7
#         additional terms, to the whole of the work, and all its parts,
#         regardless of how they are packaged.  This License gives no
#         permission to license the work in any other way, but it does not
#         invalidate such permission if you have separately received it.
#
#         d) If the work has interactive user interfaces, each must display
#         Appropriate Legal Notices; however, if the Program has interactive
#         interfaces that do not display Appropriate Legal Notices, your
#         work need not make them do so.
#
#       A compilation of a covered work with other separate and independent
#     works, which are not by their nature extensions of the covered work,
#     and which are not combined with it such as to form a larger program,
#     in or on a volume of a storage or distribution medium, is called an
#     "aggregate" if the compilation and its resulting copyright are not
#     used to limit the access or legal rights of the compilation's users
#     beyond what the individual works permit.  Inclusion of a covered work
#     in an aggregate does not cause this License to apply to the other
#     parts of the aggregate.
#
#       6. Conveying Non-Source Forms.
#
#       You may convey a covered work in object code form under the terms
#     of sections 4 and 5, provided that you also convey the
#     machine-readable Corresponding Source under the terms of this License,
#     in one of these ways:
#
#         a) Convey the object code in, or embodied in, a physical product
#         (including a physical distribution medium), accompanied by the
#         Corresponding Source fixed on a durable physical medium
#         customarily used for software interchange.
#
#         b) Convey the object code in, or embodied in, a physical product
#         (including a physical distribution medium), accompanied by a
#         written offer, valid for at least three years and valid for as
#         long as you offer spare parts or customer support for that product
#         model, to give anyone who possesses the object code either (1) a
#         copy of the Corresponding Source for all the software in the
#         product that is covered by this License, on a durable physical
#         medium customarily used for software interchange, for a price no
#         more than your reasonable cost of physically performing this
#         conveying of source, or (2) access to copy the
#         Corresponding Source from a network server at no charge.
#
#         c) Convey individual copies of the object code with a copy of the
#         written offer to provide the Corresponding Source.  This
#         alternative is allowed only occasionally and noncommercially, and
#         only if you received the object code with such an offer, in accord
#         with subsection 6b.
#
#         d) Convey the object code by offering access from a designated
#         place (gratis or for a charge), and offer equivalent access to the
#         Corresponding Source in the same way through the same place at no
#         further charge.  You need not require recipients to copy the
#         Corresponding Source along with the object code.  If the place to
#         copy the object code is a network server, the Corresponding Source
#         may be on a different server (operated by you or a third party)
#         that supports equivalent copying facilities, provided you maintain
#         clear directions next to the object code saying where to find the
#         Corresponding Source.  Regardless of what server hosts the
#         Corresponding Source, you remain obligated to ensure that it is
#         available for as long as needed to satisfy these requirements.
#
#         e) Convey the object code using peer-to-peer transmission, provided
#         you inform other peers where the object code and Corresponding
#         Source of the work are being offered to the general public at no
#         charge under subsection 6d.
#
#       A separable portion of the object code, whose source code is excluded
#     from the Corresponding Source as a System Library, need not be
#     included in conveying the object code work.
#
#       A "User Product" is either (1) a "consumer product", which means any
#     tangible personal property which is normally used for personal, family,
#     or household purposes, or (2) anything designed or sold for incorporation
#     into a dwelling.  In determining whether a product is a consumer product,
#     doubtful cases shall be resolved in favor of coverage.  For a particular
#     product received by a particular user, "normally used" refers to a
#     typical or common use of that class of product, regardless of the status
#     of the particular user or of the way in which the particular user
#     actually uses, or expects or is expected to use, the product.  A product
#     is a consumer product regardless of whether the product has substantial
#     commercial, industrial or non-consumer uses, unless such uses represent
#     the only significant mode of use of the product.
#
#       "Installation Information" for a User Product means any methods,
#     procedures, authorization keys, or other information required to install
#     and execute modified versions of a covered work in that User Product from
#     a modified version of its Corresponding Source.  The information must
#     suffice to ensure that the continued functioning of the modified object
#     code is in no case prevented or interfered with solely because
#     modification has been made.
#
#       If you convey an object code work under this section in, or with, or
#     specifically for use in, a User Product, and the conveying occurs as
#     part of a transaction in which the right of possession and use of the
#     User Product is transferred to the recipient in perpetuity or for a
#     fixed term (regardless of how the transaction is characterized), the
#     Corresponding Source conveyed under this section must be accompanied
#     by the Installation Information.  But this requirement does not apply
#     if neither you nor any third party retains the ability to install
#     modified object code on the User Product (for example, the work has
#     been installed in ROM).
#
#       The requirement to provide Installation Information does not include a
#     requirement to continue to provide support service, warranty, or updates
#     for a work that has been modified or installed by the recipient, or for
#     the User Product in which it has been modified or installed.  Access to a
#     network may be denied when the modification itself materially and
#     adversely affects the operation of the network or violates the rules and
#     protocols for communication across the network.
#
#       Corresponding Source conveyed, and Installation Information provided,
#     in accord with this section must be in a format that is publicly
#     documented (and with an implementation available to the public in
#     source code form), and must require no special password or key for
#     unpacking, reading or copying.
#
#       7. Additional Terms.
#
#       "Additional permissions" are terms that supplement the terms of this
#     License by making exceptions from one or more of its conditions.
#     Additional permissions that are applicable to the entire Program shall
#     be treated as though they were included in this License, to the extent
#     that they are valid under applicable law.  If additional permissions
#     apply only to part of the Program, that part may be used separately
#     under those permissions, but the entire Program remains governed by
#     this License without regard to the additional permissions.
#
#       When you convey a copy of a covered work, you may at your option
#     remove any additional permissions from that copy, or from any part of
#     it.  (Additional permissions may be written to require their own
#     removal in certain cases when you modify the work.)  You may place
#     additional permissions on material, added by you to a covered work,
#     for which you have or can give appropriate copyright permission.
#
#       Notwithstanding any other provision of this License, for material you
#     add to a covered work, you may (if authorized by the copyright holders of
#     that material) supplement the terms of this License with terms:
#
#         a) Disclaiming warranty or limiting liability differently from the
#         terms of sections 15 and 16 of this License; or
#
#         b) Requiring preservation of specified reasonable legal notices or
#         author attributions in that material or in the Appropriate Legal
#         Notices displayed by works containing it; or
#
#         c) Prohibiting misrepresentation of the origin of that material, or
#         requiring that modified versions of such material be marked in
#         reasonable ways as different from the original version; or
#
#         d) Limiting the use for publicity purposes of names of licensors or
#         authors of the material; or
#
#         e) Declining to grant rights under trademark law for use of some
#         trade names, trademarks, or service marks; or
#
#         f) Requiring indemnification of licensors and authors of that
#         material by anyone who conveys the material (or modified versions of
#         it) with contractual assumptions of liability to the recipient, for
#         any liability that these contractual assumptions directly impose on
#         those licensors and authors.
#
#       All other non-permissive additional terms are considered "further
#     restrictions" within the meaning of section 10.  If the Program as you
#     received it, or any part of it, contains a notice stating that it is
#     governed by this License along with a term that is a further
#     restriction, you may remove that term.  If a license document contains
#     a further restriction but permits relicensing or conveying under this
#     License, you may add to a covered work material governed by the terms
#     of that license document, provided that the further restriction does
#     not survive such relicensing or conveying.
#
#       If you add terms to a covered work in accord with this section, you
#     must place, in the relevant source files, a statement of the
#     additional terms that apply to those files, or a notice indicating
#     where to find the applicable terms.
#
#       Additional terms, permissive or non-permissive, may be stated in the
#     form of a separately written license, or stated as exceptions;
#     the above requirements apply either way.
#
#       8. Termination.
#
#       You may not propagate or modify a covered work except as expressly
#     provided under this License.  Any attempt otherwise to propagate or
#     modify it is void, and will automatically terminate your rights under
#     this License (including any patent licenses granted under the third
#     paragraph of section 11).
#
#       However, if you cease all violation of this License, then your
#     license from a particular copyright holder is reinstated (a)
#     provisionally, unless and until the copyright holder explicitly and
#     finally terminates your license, and (b) permanently, if the copyright
#     holder fails to notify you of the violation by some reasonable means
#     prior to 60 days after the cessation.
#
#       Moreover, your license from a particular copyright holder is
#     reinstated permanently if the copyright holder notifies you of the
#     violation by some reasonable means, this is the first time you have
#     received notice of violation of this License (for any work) from that
#     copyright holder, and you cure the violation prior to 30 days after
#     your receipt of the notice.
#
#       Termination of your rights under this section does not terminate the
#     licenses of parties who have received copies or rights from you under
#     this License.  If your rights have been terminated and not permanently
#     reinstated, you do not qualify to receive new licenses for the same
#     material under section 10.
#
#       9. Acceptance Not Required for Having Copies.
#
#       You are not required to accept this License in order to receive or
#     run a copy of the Program.  Ancillary propagation of a covered work
#     occurring solely as a consequence of using peer-to-peer transmission
#     to receive a copy likewise does not require acceptance.  However,
#     nothing other than this License grants you permission to propagate or
#     modify any covered work.  These actions infringe copyright if you do
#     not accept this License.  Therefore, by modifying or propagating a
#     covered work, you indicate your acceptance of this License to do so.
#
#       10. Automatic Licensing of Downstream Recipients.
#
#       Each time you convey a covered work, the recipient automatically
#     receives a license from the original licensors, to run, modify and
#     propagate that work, subject to this License.  You are not responsible
#     for enforcing compliance by third parties with this License.
#
#       An "entity transaction" is a transaction transferring control of an
#     organization, or substantially all assets of one, or subdividing an
#     organization, or merging organizations.  If propagation of a covered
#     work results from an entity transaction, each party to that
#     transaction who receives a copy of the work also receives whatever
#     licenses to the work the party's predecessor in interest had or could
#     give under the previous paragraph, plus a right to possession of the
#     Corresponding Source of the work from the predecessor in interest, if
#     the predecessor has it or can get it with reasonable efforts.
#
#       You may not impose any further restrictions on the exercise of the
#     rights granted or affirmed under this License.  For example, you may
#     not impose a license fee, royalty, or other charge for exercise of
#     rights granted under this License, and you may not initiate litigation
#     (including a cross-claim or counterclaim in a lawsuit) alleging that
#     any patent claim is infringed by making, using, selling, offering for
#     sale, or importing the Program or any portion of it.
#
#       11. Patents.
#
#       A "contributor" is a copyright holder who authorizes use under this
#     License of the Program or a work on which the Program is based.  The
#     work thus licensed is called the contributor's "contributor version".
#
#       A contributor's "essential patent claims" are all patent claims
#     owned or controlled by the contributor, whether already acquired or
#     hereafter acquired, that would be infringed by some manner, permitted
#     by this License, of making, using, or selling its contributor version,
#     but do not include claims that would be infringed only as a
#     consequence of further modification of the contributor version.  For
#     purposes of this definition, "control" includes the right to grant
#     patent sublicenses in a manner consistent with the requirements of
#     this License.
#
#       Each contributor grants you a non-exclusive, worldwide, royalty-free
#     patent license under the contributor's essential patent claims, to
#     make, use, sell, offer for sale, import and otherwise run, modify and
#     propagate the contents of its contributor version.
#
#       In the following three paragraphs, a "patent license" is any express
#     agreement or commitment, however denominated, not to enforce a patent
#     (such as an express permission to practice a patent or covenant not to
#     sue for patent infringement).  To "grant" such a patent license to a
#     party means to make such an agreement or commitment not to enforce a
#     patent against the party.
#
#       If you convey a covered work, knowingly relying on a patent license,
#     and the Corresponding Source of the work is not available for anyone
#     to copy, free of charge and under the terms of this License, through a
#     publicly available network server or other readily accessible means,
#     then you must either (1) cause the Corresponding Source to be so
#     available, or (2) arrange to deprive yourself of the benefit of the
#     patent license for this particular work, or (3) arrange, in a manner
#     consistent with the requirements of this License, to extend the patent
#     license to downstream recipients.  "Knowingly relying" means you have
#     actual knowledge that, but for the patent license, your conveying the
#     covered work in a country, or your recipient's use of the covered work
#     in a country, would infringe one or more identifiable patents in that
#     country that you have reason to believe are valid.
#
#       If, pursuant to or in connection with a single transaction or
#     arrangement, you convey, or propagate by procuring conveyance of, a
#     covered work, and grant a patent license to some of the parties
#     receiving the covered work authorizing them to use, propagate, modify
#     or convey a specific copy of the covered work, then the patent license
#     you grant is automatically extended to all recipients of the covered
#     work and works based on it.
#
#       A patent license is "discriminatory" if it does not include within
#     the scope of its coverage, prohibits the exercise of, or is
#     conditioned on the non-exercise of one or more of the rights that are
#     specifically granted under this License.  You may not convey a covered
#     work if you are a party to an arrangement with a third party that is
#     in the business of distributing software, under which you make payment
#     to the third party based on the extent of your activity of conveying
#     the work, and under which the third party grants, to any of the
#     parties who would receive the covered work from you, a discriminatory
#     patent license (a) in connection with copies of the covered work
#     conveyed by you (or copies made from those copies), or (b) primarily
#     for and in connection with specific products or compilations that
#     contain the covered work, unless you entered into that arrangement,
#     or that patent license was granted, prior to 28 March 2007.
#
#       Nothing in this License shall be construed as excluding or limiting
#     any implied license or other defenses to infringement that may
#     otherwise be available to you under applicable patent law.
#
#       12. No Surrender of Others' Freedom.
#
#       If conditions are imposed on you (whether by court order, agreement or
#     otherwise) that contradict the conditions of this License, they do not
#     excuse you from the conditions of this License.  If you cannot convey a
#     covered work so as to satisfy simultaneously your obligations under this
#     License and any other pertinent obligations, then as a consequence you may
#     not convey it at all.  For example, if you agree to terms that obligate you
#     to collect a royalty for further conveying from those to whom you convey
#     the Program, the only way you could satisfy both those terms and this
#     License would be to refrain entirely from conveying the Program.
#
#       13. Remote Network Interaction; Use with the GNU General Public License.
#
#       Notwithstanding any other provision of this License, if you modify the
#     Program, your modified version must prominently offer all users
#     interacting with it remotely through a computer network (if your version
#     supports such interaction) an opportunity to receive the Corresponding
#     Source of your version by providing access to the Corresponding Source
#     from a network server at no charge, through some standard or customary
#     means of facilitating copying of software.  This Corresponding Source
#     shall include the Corresponding Source for any work covered by version 3
#     of the GNU General Public License that is incorporated pursuant to the
#     following paragraph.
#
#       Notwithstanding any other provision of this License, you have
#     permission to link or combine any covered work with a work licensed
#     under version 3 of the GNU General Public License into a single
#     combined work, and to convey the resulting work.  The terms of this
#     License will continue to apply to the part which is the covered work,
#     but the work with which it is combined will remain governed by version
#     3 of the GNU General Public License.
#
#       14. Revised Versions of this License.
#
#       The Free Software Foundation may publish revised and/or new versions of
#     the GNU Affero General Public License from time to time.  Such new versions
#     will be similar in spirit to the present version, but may differ in detail to
#     address new problems or concerns.
#
#       Each version is given a distinguishing version number.  If the
#     Program specifies that a certain numbered version of the GNU Affero General
#     Public License "or any later version" applies to it, you have the
#     option of following the terms and conditions either of that numbered
#     version or of any later version published by the Free Software
#     Foundation.  If the Program does not specify a version number of the
#     GNU Affero General Public License, you may choose any version ever published
#     by the Free Software Foundation.
#
#       If the Program specifies that a proxy can decide which future
#     versions of the GNU Affero General Public License can be used, that proxy's
#     public statement of acceptance of a version permanently authorizes you
#     to choose that version for the Program.
#
#       Later license versions may give you additional or different
#     permissions.  However, no additional obligations are imposed on any
#     author or copyright holder as a result of your choosing to follow a
#     later version.
#
#       15. Disclaimer of Warranty.
#
#       THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
#     APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
#     HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
#     OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
#     THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#     PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
#     IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
#     ALL NECESSARY SERVICING, REPAIR OR CORRECTION.
#
#       16. Limitation of Liability.
#
#       IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
#     WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
#     THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
#     GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
#     USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
#     DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
#     PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
#     EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
#     SUCH DAMAGES.
#
#       17. Interpretation of Sections 15 and 16.
#
#       If the disclaimer of warranty and limitation of liability provided
#     above cannot be given local legal effect according to their terms,
#     reviewing courts shall apply local law that most closely approximates
#     an absolute waiver of all civil liability in connection with the
#     Program, unless a warranty or assumption of liability accompanies a
#     copy of the Program in return for a fee.
#
#                          END OF TERMS AND CONDITIONS
#
#                 How to Apply These Terms to Your New Programs
#
#       If you develop a new program, and you want it to be of the greatest
#     possible use to the public, the best way to achieve this is to make it
#     free software which everyone can redistribute and change under these terms.
#
#       To do so, attach the following notices to the program.  It is safest
#     to attach them to the start of each source file to most effectively
#     state the exclusion of warranty; and each file should have at least
#     the "copyright" line and a pointer to where the full notice is found.
#
#         <one line to give the program's name and a brief idea of what it does.>
#         Copyright (C) <year>  <name of author>
#
#         This program is free software: you can redistribute it and/or modify
#         it under the terms of the GNU Affero General Public License as published
#         by the Free Software Foundation, either version 3 of the License, or
#         (at your option) any later version.
#
#         This program is distributed in the hope that it will be useful,
#         but WITHOUT ANY WARRANTY; without even the implied warranty of
#         MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#         GNU Affero General Public License for more details.
#
#         You should have received a copy of the GNU Affero General Public License
#         along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#     Also add information on how to contact you by electronic and paper mail.
#
#       If your software can interact with users remotely through a computer
#     network, you should also make sure that it provides a way for users to
#     get its source.  For example, if your program is a web application, its
#     interface could display a "Source" link that leads users to an archive
#     of the code.  There are many ways you could offer source, and different
#     solutions will be better for different programs; see section 13 for the
#     specific requirements.
#
#       You should also get your employer (if you work as a programmer) or school,
#     if any, to sign a "copyright disclaimer" for the program, if necessary.
#     For more information on this, and how to apply and follow the GNU AGPL, see
#     <https://www.gnu.org/licenses/>.
import re
import time
from html import escape

from telegram import CallbackQuery
from telegram import ChatPermissions
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import ParseMode
from telegram.error import BadRequest
from telegram.ext import CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import run_async
from telegram.utils.helpers import mention_html

import alexa.modules.sql.welcome_sql as sql
from alexa import dispatcher
from alexa import LOGGER
from alexa import MESSAGE_DUMP
from alexa import OWNER_ID
from alexa.modules.helper_funcs.alternate import typing_action
from alexa.modules.helper_funcs.chat_status import is_user_ban_protected
from alexa.modules.helper_funcs.chat_status import user_admin
from alexa.modules.helper_funcs.chat_status import user_can_change
from alexa.modules.helper_funcs.misc import build_keyboard
from alexa.modules.helper_funcs.misc import revert_buttons
from alexa.modules.helper_funcs.msg_types import get_welcome_type
from alexa.modules.helper_funcs.string_handling import escape_invalid_curly_brackets
from alexa.modules.helper_funcs.string_handling import markdown_parser
from alexa.modules.helper_funcs.string_handling import markdown_to_html
from alexa.modules.log_channel import loggable
from alexa.modules.sql.global_bans_sql import is_user_gbanned

VALID_WELCOME_FORMATTERS = [
    "first",
    "last",
    "fullname",
    "username",
    "id",
    "count",
    "chatname",
    "mention",
]

ENUM_FUNC_MAP = {
    sql.Types.TEXT.value: dispatcher.bot.send_message,
    sql.Types.BUTTON_TEXT.value: dispatcher.bot.send_message,
    sql.Types.STICKER.value: dispatcher.bot.send_sticker,
    sql.Types.DOCUMENT.value: dispatcher.bot.send_document,
    sql.Types.PHOTO.value: dispatcher.bot.send_photo,
    sql.Types.AUDIO.value: dispatcher.bot.send_audio,
    sql.Types.VOICE.value: dispatcher.bot.send_voice,
    sql.Types.VIDEO.value: dispatcher.bot.send_video,
}

from telegram import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    Update,
)

from telegram.error import BadRequest
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,
    run_async,
)

# do not async
def send(update, message, keyboard, backup_message):
    chat = update.effective_chat
    cleanserv = sql.clean_service(chat.id)
    reply = update.message.message_id
    # Clean service welcome
    if cleanserv:
        try:
            dispatcher.bot.delete_message(chat.id, update.message.message_id)
        except BadRequest:
            pass
        reply = False
    try:
        msg = update.effective_message.reply_text(
            message,
            parse_mode=ParseMode.HTML,
            reply_markup=keyboard,
            reply_to_message_id=reply,
            disable_web_page_preview=True,
        )
    except IndexError:
        msg = update.effective_message.reply_text(
            markdown_parser(backup_message + "\nNote: the current message was "
                            "invalid due to markdown issues. Could be "
                            "due to the user's name."),
            parse_mode=ParseMode.MARKDOWN,
            reply_to_message_id=reply,
        )
    except KeyError:
        msg = update.effective_message.reply_text(
            markdown_parser(backup_message + "\nNote: the current message is "
                            "invalid due to an issue with some misplaced "
                            "curly brackets. Please update"),
            parse_mode=ParseMode.MARKDOWN,
            reply_to_message_id=reply,
        )
    except BadRequest as excp:
        if excp.message == "Button_url_invalid":
            msg = update.effective_message.reply_text(
                markdown_parser(
                    backup_message +
                    "\nNote: the current message has an invalid url "
                    "in one of its buttons. Please update."),
                parse_mode=ParseMode.MARKDOWN,
                reply_to_message_id=reply,
            )
        elif excp.message == "Unsupported url protocol":
            msg = update.effective_message.reply_text(
                markdown_parser(
                    backup_message +
                    "\nNote: the current message has buttons which "
                    "use url protocols that are unsupported by "
                    "telegram. Please update."),
                parse_mode=ParseMode.MARKDOWN,
                reply_to_message_id=reply,
            )
        elif excp.message == "Wrong url host":
            msg = update.effective_message.reply_text(
                markdown_parser(
                    backup_message +
                    "\nNote: the current message has some bad urls. "
                    "Please update."),
                parse_mode=ParseMode.MARKDOWN,
                reply_to_message_id=reply,
            )
            LOGGER.warning(message)
            LOGGER.warning(keyboard)
            LOGGER.exception("Could not parse! got invalid url host errors")
        else:
            msg = update.effective_message.reply_text(
                markdown_parser(backup_message +
                                "\nNote: An error occured when sending the "
                                "custom message. Please update."),
                parse_mode=ParseMode.MARKDOWN,
                reply_to_message_id=reply,
            )
            LOGGER.exception()

    return msg


@run_async
@spamcheck
def new_member(update, context):
    chat = update.effective_chat
    user = update.effective_user
    msg = update.effective_message
    chat_name = chat.title or chat.first or chat.username
    should_welc, cust_welcome, welc_type = sql.get_welc_pref(chat.id)
    cust_welcome = markdown_to_html(cust_welcome)
    welc_mutes = sql.welcome_mutes(chat.id)
    user_id = user.id
    human_checks = sql.get_human_checks(user_id, chat.id)
    if should_welc:
        sent = None
        new_members = update.effective_message.new_chat_members
        for new_mem in new_members:

            reply = update.message.message_id
            cleanserv = sql.clean_service(chat.id)
            # Clean service welcome
            if cleanserv:
                try:
                    dispatcher.bot.delete_message(chat.id,
                                                  update.message.message_id)
                except BadRequest:
                    pass
                reply = False

            # Ignore gbanned users
            if is_user_gbanned(new_mem.id):
                return

            # Give the owner a special welcome
            if new_mem.id == OWNER_ID:
                update.effective_message.reply_text(
                    "Master is in the house, let's get this party started!",
                    reply_to_message_id=reply,
                )
                continue

            # Make bot greet admins
            elif new_mem.id == context.bot.id:
                update.effective_message.reply_text(
                    "Hey {}, I'm {}! Thank you for adding me to {}"
                    " and be sure to join our support group: @MissAlexaRobotSupport to know more about updates and tricks!"
                    .format(user.first_name, context.bot.first_name,
                            chat_name),
                    reply_to_message_id=reply,
                )

                context.bot.send_message(
                    MESSAGE_DUMP,
                    "alexa have been added to <pre>{}</pre> with ID: \n<pre>{}</pre>"
                    .format(chat.title, chat.id),
                    parse_mode=ParseMode.HTML,
                )
            else:
                # If welcome message is media, send with appropriate function
                if welc_type != sql.Types.TEXT and welc_type != sql.Types.BUTTON_TEXT:
                    sent = ENUM_FUNC_MAP[welc_type](chat.id, cust_welcome)
                    # print(bool(sent))
                    continue
                # else, move on
                first_name = (
                    new_mem.first_name or "PersonWithNoName"
                )  # edge case of empty name - occurs for some bugs.

                if cust_welcome:
                    if new_mem.last_name:
                        fullname = "{} {}".format(first_name,
                                                  new_mem.last_name)
                    else:
                        fullname = first_name
                    count = chat.get_members_count()
                    mention = mention_html(new_mem.id, first_name)
                    if new_mem.username:
                        username = "@" + escape(new_mem.username)
                    else:
                        username = mention

                    valid_format = escape_invalid_curly_brackets(
                        cust_welcome, VALID_WELCOME_FORMATTERS)
                    res = valid_format.format(
                        first=escape(first_name),
                        last=escape(new_mem.last_name or first_name),
                        fullname=escape(fullname),
                        username=username,
                        mention=mention,
                        count=count,
                        chatname=escape(chat.title),
                        id=new_mem.id,
                    )
                    buttons = sql.get_welc_buttons(chat.id)
                    keyb = build_keyboard(buttons)
                else:
                    res = sql.DEFAULT_WELCOME.format(first=first_name)
                    keyb = []

                keyboard = InlineKeyboardMarkup(keyb)

                sent = send(update, res, keyboard,
                            sql.DEFAULT_WELCOME.format(
                                first=first_name))  # type: Optional[Message]

                # User exception from mutes:
                if (is_user_ban_protected(chat, new_mem.id,
                                          chat.get_member(new_mem.id))
                        or human_checks):
                    continue
                # Join welcome: soft mute
                if welc_mutes == "soft":
                    context.bot.restrict_chat_member(
                        chat.id,
                        new_mem.id,
                        permissions=ChatPermissions(
                            can_send_messages=True,
                            can_send_media_messages=False,
                            can_send_other_messages=False,
                            can_invite_users=False,
                            can_pin_messages=False,
                            can_send_polls=False,
                            can_change_info=False,
                            can_add_web_page_previews=False,
                            until_date=(int(time.time() + 24 * 60 * 60)),
                        ),
                    )
                # Join welcome: strong mute
                if welc_mutes == "strong":
                    new_join_mem = "Hey {}!".format(
                        mention_html(user.id, new_mem.first_name))
                    msg.reply_text(
                        "{}\nClick the button below to start talking.".format(
                            new_join_mem),
                        reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton(
                                text="Yes, I'm a human",
                                callback_data="user_join_({})".format(
                                    new_mem.id),
                            )
                        ]]),
                        parse_mode=ParseMode.HTML,
                        reply_to_message_id=reply,
                    )
                    context.bot.restrict_chat_member(
                        chat.id,
                        new_mem.id,
                        permissions=ChatPermissions(
                            can_send_messages=False,
                            can_invite_users=False,
                            can_pin_messages=False,
                            can_send_polls=False,
                            can_change_info=False,
                            can_send_media_messages=False,
                            can_send_other_messages=False,
                            can_add_web_page_previews=False,
                        ),
                    )
        prev_welc = sql.get_clean_pref(chat.id)
        if prev_welc:
            try:
                context.bot.delete_message(chat.id, prev_welc)
            except BadRequest:
                pass

            if sent:
                sql.set_clean_welcome(chat.id, sent.message_id)


@run_async
@spamcheck
def left_member(update, context):
    chat = update.effective_chat  # type: Optional[Chat]
    should_goodbye, cust_goodbye, goodbye_type = sql.get_gdbye_pref(chat.id)
    cust_goodbye = markdown_to_html(cust_goodbye)
    if should_goodbye:
        reply = update.message.message_id
        cleanserv = sql.clean_service(chat.id)
        # Clean service welcome
        if cleanserv:
            try:
                dispatcher.bot.delete_message(chat.id,
                                              update.message.message_id)
            except BadRequest:
                pass
            reply = False

        left_mem = update.effective_message.left_chat_member
        if left_mem:

            # Ignore gbanned users
            if is_user_gbanned(left_mem.id):
                return

            # Ignore bot being kicked
            if left_mem.id == context.bot.id:
                return

            # Give the owner a special goodbye
            if left_mem.id == OWNER_ID:
                update.effective_message.reply_text("RIP Master",
                                                    reply_to_message_id=reply)
                return

            # if media goodbye, use appropriate function for it
            if goodbye_type != sql.Types.TEXT and goodbye_type != sql.Types.BUTTON_TEXT:
                ENUM_FUNC_MAP[goodbye_type](chat.id, cust_goodbye)
                return

            first_name = (left_mem.first_name or "PersonWithNoName"
                          )  # edge case of empty name - occurs for some bugs.
            if cust_goodbye:
                if left_mem.last_name:
                    fullname = "{} {}".format(first_name, left_mem.last_name)
                else:
                    fullname = first_name
                count = chat.get_members_count()
                mention = mention_html(left_mem.id, first_name)
                if left_mem.username:
                    username = "@" + escape(left_mem.username)
                else:
                    username = mention

                valid_format = escape_invalid_curly_brackets(
                    cust_goodbye, VALID_WELCOME_FORMATTERS)
                res = valid_format.format(
                    first=escape(first_name),
                    last=escape(left_mem.last_name or first_name),
                    fullname=escape(fullname),
                    username=username,
                    mention=mention,
                    count=count,
                    chatname=escape(chat.title),
                    id=left_mem.id,
                )
                buttons = sql.get_gdbye_buttons(chat.id)
                keyb = build_keyboard(buttons)

            else:
                res = sql.DEFAULT_GOODBYE
                keyb = []

            keyboard = InlineKeyboardMarkup(keyb)

            send(update, res, keyboard, sql.DEFAULT_GOODBYE)


@run_async
@spamcheck
@user_can_change
def welcome(update, context):
    chat = update.effective_chat  # type: Optional[Chat]
    args = context.args
    # if no args, show current replies.
    if len(args) == 0 or args[0].lower() == "noformat":
        noformat = args and args[0].lower() == "noformat"
        pref, welcome_m, welcome_type = sql.get_welc_pref(chat.id)
        update.effective_message.reply_text(
            "This chat has it's welcome setting set to: `{}`.\n*The welcome message "
            "(not filling the {{}}) is:*".format(pref),
            parse_mode=ParseMode.MARKDOWN,
        )

        if welcome_type == sql.Types.BUTTON_TEXT:
            buttons = sql.get_welc_buttons(chat.id)
            if noformat:
                welcome_m += revert_buttons(buttons)
                update.effective_message.reply_text(welcome_m)

            else:
                keyb = build_keyboard(buttons)
                keyboard = InlineKeyboardMarkup(keyb)

                send(update, welcome_m, keyboard, sql.DEFAULT_WELCOME)

        else:
            if noformat:
                ENUM_FUNC_MAP[welcome_type](chat.id, welcome_m)

            else:
                ENUM_FUNC_MAP[welcome_type](chat.id,
                                            welcome_m,
                                            parse_mode=ParseMode.MARKDOWN)

    elif len(args) >= 1:
        if args[0].lower() in ("on", "yes"):
            sql.set_welc_preference(str(chat.id), True)
            update.effective_message.reply_text("I'll be polite!")

        elif args[0].lower() in ("off", "no"):
            sql.set_welc_preference(str(chat.id), False)
            update.effective_message.reply_text(
                "I'm sulking, not gonna greet anymore.")

        else:
            # idek what you're writing, say yes or no
            update.effective_message.reply_text(
                "I understand 'on/yes' or 'off/no' only!")


@run_async
@spamcheck
@user_can_change
def goodbye(update, context):
    chat = update.effective_chat  # type: Optional[Chat]
    args = context.args

    if len(args) == 0 or args[0] == "noformat":
        noformat = args and args[0] == "noformat"
        pref, goodbye_m, goodbye_type = sql.get_gdbye_pref(chat.id)
        update.effective_message.reply_text(
            "This chat has it's goodbye setting set to: `{}`.\n*The goodbye  message "
            "(not filling the {{}}) is:*".format(pref),
            parse_mode=ParseMode.MARKDOWN,
        )

        if goodbye_type == sql.Types.BUTTON_TEXT:
            buttons = sql.get_gdbye_buttons(chat.id)
            if noformat:
                goodbye_m += revert_buttons(buttons)
                update.effective_message.reply_text(goodbye_m)

            else:
                keyb = build_keyboard(buttons)
                keyboard = InlineKeyboardMarkup(keyb)

                send(update, goodbye_m, keyboard, sql.DEFAULT_GOODBYE)

        else:
            if noformat:
                ENUM_FUNC_MAP[goodbye_type](chat.id, goodbye_m)

            else:
                ENUM_FUNC_MAP[goodbye_type](chat.id,
                                            goodbye_m,
                                            parse_mode=ParseMode.MARKDOWN)

    elif len(args) >= 1:
        if args[0].lower() in ("on", "yes"):
            sql.set_gdbye_preference(str(chat.id), True)
            update.effective_message.reply_text(
                "I'll be sorry when people leave!")

        elif args[0].lower() in ("off", "no"):
            sql.set_gdbye_preference(str(chat.id), False)
            update.effective_message.reply_text(
                "They leave, they're dead to me.")

        else:
            # idek what you're writing, say yes or no
            update.effective_message.reply_text(
                "I understand 'on/yes' or 'off/no' only!")


@run_async
@spamcheck
@user_can_change
@loggable
def set_welcome(update, context) -> str:
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]

    text, data_type, content, buttons = get_welcome_type(msg)

    if data_type is None:
        msg.reply_text("You didn't specify what to reply with!")
        return ""

    sql.set_custom_welcome(chat.id, content or text, data_type, buttons)
    msg.reply_text("Successfully set custom welcome message!")

    return ("<b>{}:</b>"
            "\n#SET_WELCOME"
            "\n<b>Admin:</b> {}"
            "\nSet the welcome message.".format(
                escape(chat.title), mention_html(user.id, user.first_name)))


@run_async
@spamcheck
@user_can_change
@loggable
def reset_welcome(update, context) -> str:
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    sql.set_custom_welcome(chat.id, sql.DEFAULT_WELCOME, sql.Types.TEXT)
    update.effective_message.reply_text(
        "Successfully reset welcome message to default!")
    return ("<b>{}:</b>"
            "\n#RESET_WELCOME"
            "\n<b>Admin:</b> {}"
            "\nReset the welcome message to default.".format(
                escape(chat.title), mention_html(user.id, user.first_name)))


@run_async
@spamcheck
@user_can_change
@loggable
def set_goodbye(update, context) -> str:
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]
    text, data_type, content, buttons = get_welcome_type(msg)

    if data_type is None:
        msg.reply_text("You didn't specify what to reply with!")
        return ""

    sql.set_custom_gdbye(chat.id, content or text, data_type, buttons)
    msg.reply_text("Successfully set custom goodbye message!")
    return ("<b>{}:</b>"
            "\n#SET_GOODBYE"
            "\n<b>Admin:</b> {}"
            "\nSet the goodbye message.".format(
                escape(chat.title), mention_html(user.id, user.first_name)))


@run_async
@spamcheck
@user_can_change
@loggable
def reset_goodbye(update, context) -> str:
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    sql.set_custom_gdbye(chat.id, sql.DEFAULT_GOODBYE, sql.Types.TEXT)
    update.effective_message.reply_text(
        "Successfully reset goodbye message to default!")
    return ("<b>{}:</b>"
            "\n#RESET_GOODBYE"
            "\n<b>Admin:</b> {}"
            "\nReset the goodbye message.".format(
                escape(chat.title), mention_html(user.id, user.first_name)))


@run_async
@spamcheck
@user_can_change
@loggable
def welcomemute(update, context) -> str:
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    msg = update.effective_message  # type: Optional[Message]
    args = context.args

    if len(args) >= 1:
        if args[0].lower() in ("off", "no"):
            sql.set_welcome_mutes(chat.id, False)
            msg.reply_text("I will no longer mute people on joining!")
            return ("<b>{}:</b>"
                    "\n#WELCOME_MUTE"
                    "\n<b>• Admin:</b> {}"
                    "\nHas toggled welcome mute to <b>OFF</b>.".format(
                        escape(chat.title),
                        mention_html(user.id, user.first_name)))
        elif args[0].lower() in ("soft"):
            sql.set_welcome_mutes(chat.id, "soft")
            msg.reply_text(
                "I will restrict user's permission to send media for 24 hours")
            return ("<b>{}:</b>"
                    "\n#WELCOME_MUTE"
                    "\n<b>• Admin:</b> {}"
                    "\nHas toggled welcome mute to <b>SOFT</b>.".format(
                        escape(chat.title),
                        mention_html(user.id, user.first_name)))
        elif args[0].lower() in ("strong"):
            sql.set_welcome_mutes(chat.id, "strong")
            msg.reply_text("I will now mute people when they join and"
                           " click on the button to be unmuted.")
            return ("<b>{}:</b>"
                    "\n#WELCOME_MUTE"
                    "\n<b>• Admin:</b> {}"
                    "\nHas toggled welcome mute to <b>STRONG</b>.".format(
                        escape(chat.title),
                        mention_html(user.id, user.first_name)))
        else:
            msg.reply_text(
                "Please enter `off`/`on`/`soft`/`strong`!",
                parse_mode=ParseMode.MARKDOWN,
            )
            return ""
    else:
        curr_setting = sql.welcome_mutes(chat.id)
        reply = "\n Give me a setting! Choose one of: `off`/`no` or `soft` or `strong` only! \nCurrent setting: `{}`"
        msg.reply_text(reply.format(curr_setting),
                       parse_mode=ParseMode.MARKDOWN)
        return ""


@run_async
@spamcheck
@user_can_change
@loggable
def clean_welcome(update, context) -> str:
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    args = context.args

    if not args:
        clean_pref = sql.get_clean_pref(chat.id)
        if clean_pref:
            update.effective_message.reply_text(
                "I should be deleting welcome messages up to two days old.")
        else:
            update.effective_message.reply_text(
                "I'm currently not deleting old welcome messages!")
        return ""

    if args[0].lower() in ("on", "yes"):
        sql.set_clean_welcome(str(chat.id), True)
        update.effective_message.reply_text(
            "I'll try to delete old welcome messages!")
        return ("<b>{}:</b>"
                "\n#CLEAN_WELCOME"
                "\n<b>Admin:</b> {}"
                "\nHas toggled clean welcomes to <code>ON</code>.".format(
                    escape(chat.title), mention_html(user.id,
                                                     user.first_name)))
    elif args[0].lower() in ("off", "no"):
        sql.set_clean_welcome(str(chat.id), False)
        update.effective_message.reply_text(
            "I won't delete old welcome messages.")
        return ("<b>{}:</b>"
                "\n#CLEAN_WELCOME"
                "\n<b>Admin:</b> {}"
                "\nHas toggled clean welcomes to <code>OFF</code>.".format(
                    escape(chat.title), mention_html(user.id,
                                                     user.first_name)))
    else:
        # idek what you're writing, say yes or no
        update.effective_message.reply_text(
            "I understand 'on/yes' or 'off/no' only!")
        return ""


@run_async
@spamcheck
@user_can_change
def cleanservice(update: Update, context: CallbackContext) -> str:
    args = context.args
    chat = update.effective_chat  # type: Optional[Chat]
    if chat.type != chat.PRIVATE:
        if len(args) >= 1:
            var = args[0]
            if var in ("no", "off"):
                sql.set_clean_service(chat.id, False)
                update.effective_message.reply_text(
                    "Welcome clean service is : off")
            elif var in ("yes", "on"):
                sql.set_clean_service(chat.id, True)
                update.effective_message.reply_text(
                    "Welcome clean service is : on")
            else:
                update.effective_message.reply_text(
                    "Invalid option", parse_mode=ParseMode.MARKDOWN)
        else:
            update.effective_message.reply_text(
                "Usage is on/yes or off/no", parse_mode=ParseMode.MARKDOWN)
    else:
        curr = sql.clean_service(chat.id)
        if curr:
            update.effective_message.reply_text(
                "Welcome clean service is : on", parse_mode=ParseMode.MARKDOWN)
        else:
            update.effective_message.reply_text(
                "Welcome clean service is : off", parse_mode=ParseMode.MARKDOWN)



@run_async
@spamcheck
def user_button(update, context):
    chat = update.effective_chat  # type: Optional[Chat]
    user = update.effective_user  # type: Optional[User]
    query = update.callback_query  # type: Optional[CallbackQuery]
    match = re.match(r"user_join_\((.+?)\)", query.data)
    message = update.effective_message  # type: Optional[Message]
    db_checks = sql.set_human_checks(user.id, chat.id)
    join_user = int(match.group(1))

    if join_user == user.id:
        query.answer(text="Yus! You're a human, Unmuted!")
        context.bot.restrict_chat_member(
            chat.id,
            user.id,
            permissions=ChatPermissions(
                can_send_messages=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_send_polls=True,
                can_change_info=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
            ),
        )
        context.bot.deleteMessage(chat.id, message.message_id)
        db_checks
    else:
        query.answer(text="You're not allowed to do this!")


WELC_HELP_TXT = (
    "Your group's welcome/goodbye messages can be personalised in multiple ways. If you want the messages"
    " to be individually generated, like the default welcome message is, you can use *these* variables:\n"
    " - `{{first}}`: this represents the user's *first* name\n"
    " - `{{last}}`: this represents the user's *last* name. Defaults to *first name* if user has no "
    "last name.\n"
    " - `{{fullname}}`: this represents the user's *full* name. Defaults to *first name* if user has no "
    "last name.\n"
    " - `{{username}}`: this represents the user's *username*. Defaults to a *mention* of the user's "
    "first name if has no username.\n"
    " - `{{mention}}`: this simply *mentions* a user - tagging them with their first name.\n"
    " - `{{id}}`: this represents the user's *id*\n"
    " - `{{count}}`: this represents the user's *member number*.\n"
    " - `{{chatname}}`: this represents the *current chat name*.\n"
    "\nEach variable MUST be surrounded by `{{}}` to be replaced.\n"
    "Welcome messages also support markdown, so you can make any elements bold/italic/code/links. "
    "Buttons are also supported, so you can make your welcomes look awesome with some nice intro "
    "buttons.\n"
    "To create a button linking to your rules, use this: `[Rules](buttonurl://t.me/{}?start=group_id)`. "
    "Simply replace `group_id` with your group's id, which can be obtained via /id, and you're good to "
    "go. Note that group ids are usually preceded by a `-` sign; this is required, so please don't "
    "remove it.\n"
    "If you're feeling fun, you can even set images/gifs/videos/voice messages as the welcome message by "
    "replying to the desired media, and calling /setwelcome.".format(
        dispatcher.bot.username))


@run_async
@spamcheck
@user_can_change
def welcome_help(update, context):
    update.effective_message.reply_text(WELC_HELP_TXT,
                                        parse_mode=ParseMode.MARKDOWN)


# TODO: get welcome data from group butler snap
# def __import_data__(chat_id, data):
#     welcome = data.get('info', {}).get('rules')
#     welcome = welcome.replace('$username', '{username}')
#     welcome = welcome.replace('$name', '{fullname}')
#     welcome = welcome.replace('$id', '{id}')
#     welcome = welcome.replace('$title', '{chatname}')
#     welcome = welcome.replace('$surname', '{lastname}')
#     welcome = welcome.replace('$rules', '{rules}')
#     sql.set_custom_welcome(chat_id, welcome, sql.Types.TEXT)


def __migrate__(old_chat_id, new_chat_id):
    sql.migrate_chat(old_chat_id, new_chat_id)


def __chat_settings__(chat_id, user_id):
    welcome_pref, _, _ = sql.get_welc_pref(chat_id)
    goodbye_pref, _, _ = sql.get_gdbye_pref(chat_id)
    clean_welc_pref = sql.get_clean_pref(chat_id)
    welc_mutes_pref = sql.get_welc_mutes_pref(chat_id)
    return ("This chat has it's welcome preference set to `{}`.\n"
            "It's goodbye preference is `{}`. \n\n"
            "*Service preferences:*\n"
            "\nClean welcome: `{}`"
            "\nWelcome mutes: `{}`".format(welcome_pref, goodbye_pref,
                                           clean_welc_pref, welc_mutes_pref))


__mod_name__ = "Greetings"

NEW_MEM_HANDLER = MessageHandler(Filters.status_update.new_chat_members,
                                 new_member)
LEFT_MEM_HANDLER = MessageHandler(Filters.status_update.left_chat_member,
                                  left_member)
WELC_PREF_HANDLER = CommandHandler("welcome",
                                   welcome,
                                   pass_args=True,
                                   filters=Filters.group)
GOODBYE_PREF_HANDLER = CommandHandler("goodbye",
                                      goodbye,
                                      pass_args=True,
                                      filters=Filters.group)
SET_WELCOME = CommandHandler("setwelcome", set_welcome, filters=Filters.group)
SET_GOODBYE = CommandHandler("setgoodbye", set_goodbye, filters=Filters.group)
RESET_WELCOME = CommandHandler("resetwelcome",
                               reset_welcome,
                               filters=Filters.group)
RESET_GOODBYE = CommandHandler("resetgoodbye",
                               reset_goodbye,
                               filters=Filters.group)
CLEAN_WELCOME = CommandHandler("cleanwelcome",
                               clean_welcome,
                               pass_args=True,
                               filters=Filters.group)
WELCOMEMUTE_HANDLER = CommandHandler("welcomemute",
                                     welcomemute,
                                     pass_args=True,
                                     filters=Filters.group)
CLEAN_SERVICE_HANDLER = CommandHandler("cleanservice",
                                       cleanservice,
                                       pass_args=True,
                                       filters=Filters.group)
WELCOME_HELP = CommandHandler("welcomehelp", welcome_help)
BUTTON_VERIFY_HANDLER = CallbackQueryHandler(user_button,
                                             pattern=r"user_join_")

dispatcher.add_handler(NEW_MEM_HANDLER)
dispatcher.add_handler(LEFT_MEM_HANDLER)
dispatcher.add_handler(WELC_PREF_HANDLER)
dispatcher.add_handler(GOODBYE_PREF_HANDLER)
dispatcher.add_handler(SET_WELCOME)
dispatcher.add_handler(SET_GOODBYE)
dispatcher.add_handler(RESET_WELCOME)
dispatcher.add_handler(RESET_GOODBYE)
dispatcher.add_handler(CLEAN_WELCOME)
dispatcher.add_handler(WELCOMEMUTE_HANDLER)
dispatcher.add_handler(CLEAN_SERVICE_HANDLER)
dispatcher.add_handler(BUTTON_VERIFY_HANDLER)
dispatcher.add_handler(WELCOME_HELP)
