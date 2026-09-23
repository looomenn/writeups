import re

# The characters used in encryption.
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}~_"
modulus = 67


def bigram_multiplicative_shift(bigram):
    """
    Encrypts a two-character plaintext bigram.
    Positions are 1-indexed (i.e. 'a' → 1, ..., '_' → 66).
    Computes:
         shift = (pos1 * pos2) % 67
         c1 = characters[((pos1 * shift) % 67) - 1]
         c2 = characters[((pos2 * shift) % 67) - 1]
    Returns the ciphertext bigram.
    """
    assert len(bigram) == 2, "Bigram must have length 2."
    pos1 = characters.find(bigram[0]) + 1
    pos2 = characters.find(bigram[1]) + 1
    shift = (pos1 * pos2) % modulus
    # Note: since our arithmetic is modulo 67 and our valid numbers are 1..66,
    # the result of (… % 67) is in 0..66 and subtracting 1 yields an index in  -1..65.
    # In Python an index of -1 returns the last character.
    c1 = characters[((pos1 * shift) % modulus) - 1]
    c2 = characters[((pos2 * shift) % modulus) - 1]
    return c1 + c2


#############################################
# Step 1. Build the inverse mapping dictionary
#############################################

# For every possible plaintext bigram (66*66 possibilities), compute its ciphertext.
# (Because the mapping is many-to-one, many plaintext bigrams may produce the same ciphertext.)
inverse_map = {}  # will map: ciphertext bigram  ->  list of plaintext bigrams
for ch1 in characters:
    for ch2 in characters:
        plaintext_bigram = ch1 + ch2
        cipher_bigram = bigram_multiplicative_shift(plaintext_bigram)
        inverse_map.setdefault(cipher_bigram, []).append(plaintext_bigram)

#############################################
# Step 2. Prepare the ciphertexts and split them into bigrams.
#############################################

# These three strings are given:
ciphertext_flag = "jlT84CKOAhxvdrPQWlWT6cEVD78z5QREBINSsU50FMhv662W"
not_the_flag = "mCtRNrPw_Ay9mytTR7ZpLJtrflqLS0BLpthi~2LgUY9cii7w"
also_not_the_flag = "PKRcu0l}D823P2R8c~H9DMc{NmxDF{hD3cB~i1Db}kpR77iU"


def split_into_bigrams(text):
    if len(text) % 2 != 0:
        raise ValueError("Text length must be even.")
    return [text[i:i + 2] for i in range(0, len(text), 2)]


# Split each ciphertext into its bigrams.
cipher_bigrams_flag = split_into_bigrams(ciphertext_flag)
cipher_bigrams_not_flag = split_into_bigrams(not_the_flag)
cipher_bigrams_also_not = split_into_bigrams(also_not_the_flag)

#############################################
# Step 3. Decrypt by combining candidate plaintext bigrams.
#############################################

# We know the flag must have the format "lactf{ ... }"
flag_prefix = "lactf{"
flag_pattern = re.compile(r"^lactf\{.*\}$")


def decrypt_ciphertext(cipher_bigrams):
    # For each ciphertext bigram, get its candidate plaintext bigrams.
    candidate_lists = []
    for idx, bigram in enumerate(cipher_bigrams):
        candidates = inverse_map.get(bigram, [])
        if not candidates:
            raise ValueError(f"No candidates found for ciphertext bigram: {bigram}")
        candidate_lists.append(candidates)
    print("Number of candidates per bigram:")
    for i, clist in enumerate(candidate_lists):
        print(f"  Bigram {i}: {len(clist)} candidates")

    # Use iterative dynamic programming to combine candidates while propagating constraints.
    # We'll build a set of candidate plaintext strings, one bigram at a time.
    # Start with an empty string.
    possible = {""}
    for i, candidates in enumerate(candidate_lists):
        new_possible = set()
        for prefix in possible:
            for cand in candidates:
                new_text = prefix + cand
                # If we haven't reached the length of the prefix "lactf{", enforce it.
                if len(new_text) < len(flag_prefix):
                    if not flag_prefix.startswith(new_text):
                        continue
                new_possible.add(new_text)
        possible = new_possible
        print(
            f"After processing bigram {i + 1}/{len(candidate_lists)}: {len(possible)} possibilities"
            )
        if not possible:
            break

    # At this point, each element in 'possible' is a candidate full plaintext.
    # Filter out those that match our overall flag format.
    return [p for p in possible if flag_pattern.fullmatch(p)]


#############################################
# Step 4. Run the decryption for each provided string.
#############################################

print("\nDecrypting the main flag candidate...")
decrypted_flags = decrypt_ciphertext(cipher_bigrams_flag)
print("Decrypted flag candidates:")
for flag in decrypted_flags:
    print(flag)

print("\nDecrypting not_the_flag...")
decrypted_not_flag = decrypt_ciphertext(cipher_bigrams_not_flag)
print("Decrypted not_the_flag candidates:")
for candidate in decrypted_not_flag:
    print(candidate)

print("\nDecrypting also_not_the_flag...")
decrypted_also_not_flag = decrypt_ciphertext(cipher_bigrams_also_not)
print("Decrypted also_not_the_flag candidates:")
for candidate in decrypted_also_not_flag:
    print(candidate)
